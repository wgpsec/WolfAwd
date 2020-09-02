<h1 align="center">WolfAWD 🛠</h1>

<p>
  <img src="https://img.shields.io/badge/Language-Python3-blue" />
  <img src="https://img.shields.io/badge/Version-0.1-blue" />
</p>

# 项目介绍

目前github上还没有一个将AWD框架做到可视化的项目，随着近些年CTF比赛越发的盛行，越来越多的awd脚本需求出现了，这个项目就是想要做出目前第一个也就是独一份的AWD比赛可视化辅助脚本，可以让参赛选手在比赛中腾出更多的时间来进行代码审计，也可以为新人节省更多的精力

![](doc/img/diagram.jpg)

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

## 数据表结构 （语雀完善中）

### poc



| 字段名称 |     类型     | 说明                                 |
| :------: | :----------: | ------------------------------------ |
|    id    |     int      | 索引（自增id）                       |
|   name   | varchar（30) | 名称                                 |
|   type   |    int(2)    | 类型 0 flag 1 webshell 2 systemshell |
|    os    |              | 系统类别0 php1 python                |



### targeta

|     字段名称     |     类型     | 说明           |
| :--------------: | :----------: | -------------- |
|        id        |     int      | 索引（自增id） |
|        ip        | varchar（30) | 名称           |
|   ims_connect    |              | 类型           |
|   is_get_shell   |              | 系统类别       |
|       flag       |              |                |
| flag_create_time |              |                |

### 流量

| 字段名称   | 类型         | 说明            |
| ---------- | ------------ | --------------- |
| id         | int          | 索引（自增id）  |
| message    | varchar（30) | 名称            |
| type       |              | 类型 (get post) |
| host       |              | 系统类别        |
| source_ip  |              |                 |
| create_ime |              |                 |

## 需求

https://github.com/orgs/wgpsec/projects/3

暂时想到这么多，师傅们有想法请加进去



# 更新日志

- 2020-08-31 
  
  - 完成第一版初版
  
- 2020-9-1
  - 加入SSH连接功能
  
- 2020-9-2
  - 加入命令发送全部主机功能
  
    
  
    