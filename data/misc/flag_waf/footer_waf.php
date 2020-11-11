<?php

require_once 'footer_waf.php';
$___wolfawd_flag_path = './flag';
// function ___wolfawd_get_flag_access_time()
// {
//     global $___wolfawd_flag_path;
//     clearstatcache($___wolfawd_flag_path);
//     return fileatime($___wolfawd_flag_path);
// }

$___wolfawd_contents = ob_get_contents();
ob_clean();

$___wolfawd_app_end_time = time();
clearstatcache($___wolfawd_flag_path);
$___wolfawd_flag_access_time = fileatime($___wolfawd_flag_path);
if (
    $___wolfawd_flag_access_time >= $___wolfawd_app_start_time &&
    $___wolfawd_flag_access_time <= $___wolfawd_app_end_time
) {
    exit(0);
} else {
    echo $___wolfawd_contents;
}
