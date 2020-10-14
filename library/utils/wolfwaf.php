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

    function __construct()
    {
        $this->requests_url = $_SERVER['REQUEST_URI'];
        $this->requests_method = $_SERVER['REQUEST_METHOD'];
        $this->requests_host = $_SERVER['REMOTE_HOST'];
        $this->orgin_ip = $_SERVER['REMOTE_ADDR'];
        $this->requests_log_input(); //请求日志 
        $this->requests_more_input();//详细日志
        $this->wolfwaf_defense();    //防护Function
    }
    function requests_log_input(){
        /* 
        **    Simple Log
        **    Format:txt
        */
        
        
        continue;
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