## 线下赛攻击框架

### run.py

-m 指定模块
-a 指定行为
e
- attack模块
    - shell 利用vuln执行命令 -e 指定要执行的命令
    - get_flag 获取flag并且提交
    - get_shell 写入一句话
    - get_undead_shell 写入不死马
    - get_worm_shell 写入蠕虫马
- guard模块
  
### 设计思路

因为以前的设计过于繁琐,距离可以用遥遥无期,因此参考另一个框架对项目进行重构

基本想法,框架会加载games下poc,需要传入-m参数,指定要加载的poc
加载后,根据用户传入的指令,例如get_flag 调用library下的all_attatck.py中的函数,生成cmd命令,然后利用poc执行,cmd支持返回字符串或者元组,元组内容为(执行的命令,回调函数),例如执行的命令可以为 cat /flag ,然后在回调函数中 获取flag并且提交,框架获取到此种类型的cmd时,会在获取命令执行结果后,执行回调函数
同时框架支持执行利用poc进行权限维持,例如上传不死马,下次get_flag会首先,会先利用不死马进行get_flag

### 使用方法

设置好games目录下的submit_flag 和targets 并且利用poc_test和flag_test进行测试

编写poc
利用框架自动化攻击

```

    parser = OptionParser()
    parser.add_option("-m", "--module", \
                      dest="module", default="attack", \
                      help="Input the  func module here :)")
    parser.add_option("-p", "--poc", \
                      dest="vuln", default="chinaz",
                      help="The vuln you want to use")
    parser.add_option("-a", "--action", \
                      dest="action", default="get_flag",
                      help="The action you want to do")
    parser.add_option("-c", "--command", \
                      dest="command", default="",
                      help="The command you want to exec")
    parser.add_option("-t", "--targets", \
                      dest="targets", default="",
                      help="The target you want to attack")
    (options, args) = parser.parse_args()

    return options
```
示例命令:

```
通过漏洞利用文件chinaz获取flag,仅显示,支持使用多个poc文件以空格分割
python3  run.py -p chinaz -a get_flag
自动获取并且提交flag
python3  run.py -p chinaz -a submit_flag
利用漏洞上传不死马
python3  run.py -p chinaz -a submit_flag upload_backdoor
自动获取并且提交flag,循环执行99999次,每180s执行一次
python3  run.py  -p chinaz -a submit_flag -l 99999 -s 180
```

## TO-DO
- [ ] 根据ip段快速生成targets文件
- [ ] 编写防御模块
- [ ] 使用协程或者多线程重构逻辑
- [ ] 重构cmd模块逻辑,对php eval和system和读flag分开处理
- [ ] 增加利用蠕虫马维持权限
- [ ] 统一整个框架的请求类

