﻿<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>xxx525管理系统</title>
 <!--  <meta name="description" content="particles.js is a lightweight JavaScript library for creating particles.">
  <meta name="author" content="Vincent Garreau" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"> -->
  <link rel="stylesheet" media="screen" href="public/css/style.css">
	<link rel="stylesheet" type="text/css" href="public/css/reset.css"/>
	<style>
	#particles-js{
		width: 100%;
		height: 100%;
		position: relative;
		background-image: url(public/image/bg.jpg);
		background-position: 50% 50%;
		background-size: cover;
		background-repeat: no-repeat;
		margin-left: auto;
		margin-right: auto;
}
	
	</style>
</head>
<body>
<form   class="form-signin" id="test2" method="post" action="./index.php?c=User&a=register">
<div id="particles-js">
		<div class="login">
			<div class="login-top" style="margin-top: 75px;">
				学生会-简历系统
			</div>
			<div class="login-center clearfix">
				<div class="login-center-img"><img src="public/image/name.png"/></div>
				<div class="login-center-input">
					<input type="text" name="username" placeholder="请输入您名字（用户名）" onfocus="this.placeholder=''" onblur="this.placeholder='请输入您的用户名'" required autofocus/>
					<div class="login-center-input-text">用户名</div>
				</div>
			</div>
			<div class="login-center clearfix">
				<div class="login-center-img"><img src="public/image/password.png"/></div>
				<div class="login-center-input">
					<input type="password" name="password" placeholder="请输入您的密码" onfocus="this.placeholder=''" onblur="this.placeholder='请输入您的密码'" required/>
					<div class="login-center-input-text">密码</div>
				</div>
			</div>
			<div class="login-center clearfix">
					<div class="login-center-img"><img src="public/image/password.png"/></div>
					<div class="login-center-input">
						<input type="radio" name="sex" id="xqfs_sub1" value="0" style="margin-top: 12px; height: 14px; width: 14px;  margin-left: 10px"/><label style="font-size: 18px; padding: 20px; color: #a5a3a3;">男</label>
              <input type="radio" name="sex" id="xqfs_sub2" value="1" style="margin-top: 12px; height: 14px; width: 14px;"/><label style="font-size: 18px; padding: 20px; color: #a5a3a3;">女</label>
						<div class="login-center-input-text">性别</div>
					</div>
				</div>
				<div class="login-center clearfix">
						<div class="login-center-img"><img src="public/image/password.png"/></div>
						<div class="login-center-input">
							<input type="number" name="age" placeholder="请输入您的年龄" onfocus="this.placeholder=''" onblur="this.placeholder='请输入您的年龄'" required/>
							<div class="login-center-input-text">年龄</div>
						</div>
					</div>
        <div class="login-button">
          <input  style="width:100%;height:100%;color:white;background-color:transparent;border:0;" type="submit" value="注册">
        </div>
		<div class="sk-rotating-plane"></div>
</div>

<!-- scripts -->
<script src="public/js/particles.min.js"></script>
<script src="public/js/app.js"></script>
<script type="text/javascript">
	function hasClass(elem, cls) {
	  cls = cls || '';
	  if (cls.replace(/\s/g, '').length == 0) return false; //当cls没有参数时，返回false
	  return new RegExp(' ' + cls + ' ').test(' ' + elem.className + ' ');
	}
	 
	function addClass(ele, cls) {
	  if (!hasClass(ele, cls)) {
	    ele.className = ele.className == '' ? cls : ele.className + ' ' + cls;
	  }
	}
	 
	function removeClass(ele, cls) {
	  if (hasClass(ele, cls)) {
	    var newClass = ' ' + ele.className.replace(/[\t\r\n]/g, '') + ' ';
	    while (newClass.indexOf(' ' + cls + ' ') >= 0) {
	      newClass = newClass.replace(' ' + cls + ' ', ' ');
	    }
	    ele.className = newClass.replace(/^\s+|\s+$/g, '');
	  }
	}
</script>
</form>
</body>
</html>