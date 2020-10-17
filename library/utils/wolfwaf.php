<?php
/* 
** WolfAWD内嵌 PHPWaf
**      WgpSec 
** http://www.wgpsec.org
 */
error_reporting(0);

class WolfWaf{

    private $requests_url;
    private $requests_host;
    private $orgin_ip;
    private $requests_data;
    private $requests_method;
    private $log_file_simple;
    private $log_file_detailed;

    function __construct()
    {
        $this->requests_url = $_SERVER['REQUEST_URI'];
        $this->requests_method = $_SERVER['REQUEST_METHOD'];
        $this->requests_host = $_SERVER['REMOTE_HOST'];
        $this->orgin_ip = $_SERVER['REMOTE_ADDR'];
        $this->requests_data = file_get_contents('php://input');
        $this->log_file_simple = "log_simple.txt";
        $this->log_file_detailed = "log_detailed.txt";
        $this->requests_log_input(); //请求日志 
        $this->requests_more_input();//详细日志
        $this->wolfwaf_defense();    //防护Function
    }
    function requests_log_input(){
        /* 
        **    Simple Log
        **    Format:txt
        */
        $this->contents = date("Y/m/d H:i:s") . "\t";
        $this->contents .= $this->requests_method . "\t";
        $this->contents .= $this->orgin_ip . "\t";
        $this->contents .= $this->requests_url . "\t" ;
        if ($this->requests_method == 'POST'){
            $this->contents .= "POST_DATA:" . $this->requests_data . "\n";
        }
        else{
            $this->contents .= "\n";
        }
        $log_file = fopen($this->log_file_simple,'a');
        fwrite($log_file , $this->contents);
        fclose($log_file);
        $this->contents = null;

    }   
    function requests_more_input(){
        /* 
        **    Detailed Log
        **    Format:txt
        */
        continue;
    }
    function wolfwaf_defense(){
        /*
        **    Main defense function
        */
        continue;
    }
    
    
    
}
?>