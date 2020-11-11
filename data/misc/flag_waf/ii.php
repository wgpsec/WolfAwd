<?php
// / $___wolfawd_flag_path = /flag';

// / function ___wolfawd_get_flag_access_time()
// / {
// /     global $___wolfawd_flag_path;
// /     clearstatcache();
// /     return fileatime($___wolfawd_flag_path);
// / }

// / echo ___wolfawd_get_flag_access_time();
// / readfile(/flag');
// / echo '______' . ___wolfawd_get_flag_access_time();
// / echo '___' . ___wolfawd_get_flag_access_time();
// / readfile(/flag');
// / echo '__' . ___wolfawd_get_flag_access_time();

clearstatcache('/flag');
echo fileatime('/flag');
echo '---';
clearstatcache('/flag');
echo '---';
echo fileatime('/flag');
echo '---';
sleep(2);
readfile('/flag');
sleep(2);
echo '---';
clearstatcache('/flag');
echo '---';
echo fileatime('/flag');
echo '---';
