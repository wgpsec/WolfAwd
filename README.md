# WolfAwd

## 基本想法

利用 mvc 框架，显示和功能分离，
每次比赛的数据都放在到 games 里

## 目录结构

├── data # 框架运行所需要的持久化文件
├── games  
├── library  
│ ├── controller
│ │ ├── common
│ │ ├── defense
│ │ └── exploit
│ ├── models
│ └── views
│ │ ├── common
│ │ ├── defense
│ │ └── exploit
│ ├── common
│ ├── defense
│ └── exploit
├── config.py
├── README.md
└── requirements.txt

## 数据表结构

```

targeta
id  ip     ims_connect  is_get_shell   flag  flag_create_time

poc
id  name type                         os
0 php
1 python
0 flag
1  webshell
2  systemshell

network_flow
id message         type   host  source_ip   create_ime
get
post
其他

```

## 需求

https://github.com/orgs/wgpsec/projects/3

暂时想到这么多，师傅们有想法请加进去
