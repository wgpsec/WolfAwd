<?php
// 感染的检查头,准备加上检查这个页面和计算比对指定行之间的md5
$tips = 'AWD_wolf_Check';
// 感染页面的代码开始行
$code_start_line = '172';


class AWDWorm
{
    private static  $instance;
    // 扫到的文件
    protected $SCAN_FILE_ARR = array();
    protected $SCAN_DIR_ARR = array();
    private function __construct()
    {
        array_push($this->SCAN_DIR_ARR, $_SERVER["DOCUMENT_ROOT"] ? $_SERVER["DOCUMENT_ROOT"] : "/var/www/htm/");
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
        $content = file_get_contents($file);
        $content_line = explode("\n", $content);

        return false;
    }
    public function infectFile($file)
    {
        // do nothing
        var_dump($file);
    }
}

AWDWorm::getInstance()->scanDir();
