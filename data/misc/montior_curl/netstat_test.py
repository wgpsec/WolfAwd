#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-12 08:44:38
# @Author  : Nero 
# @Link    : N/A
# @Version : 3.0

'''
更新功能：
更新记录：
---2020-05-16 v3.0：
    1. 增加多线程，优化逻辑结构
---2020-05-12 v2.0：
    1. 增加黑、白名单模式；
    2. 输入进程名称时对大小写不敏感；
    3. 过滤进程增加模式匹配，不再需要完整写入进程名称，如要过滤chrome.exe进程，输入chro即可；
    4. 优化显示格式；
    5. 修改时间戳为人类模式
'''

import psutil,netaddr,time,re,threading


class init(object):

    def __init__(self):
        pass

    def input_legal_judge(self,mode):
        pass

    def start(self):
        pass

    def multi_threading():
        pass


class Collect(init):

    def __init__(self):
        super(Collect,self).__init__()
        self.record=[]

    def input_legal_judge(mode):
        """输入合法性判断"""
        while 1:

            if mode in ["0","1"]:
                return mode
            elif mode in [None,""]:
                mode = "1"
                return mode
            else:
                mode = input("input Error, try again：\n 0 White_list\n 1 Black_list\nenter code(0 or 1): ")


    #------------------信息收集------------------------
    def collect_func(self,flag=False):
        # record= []                      #用于存放筛选后的数据，作为函数返回值
        #筛选符合条件的数据
        while flag:
            for session in psutil.net_connections(kind="all"):
                if session.laddr and session.raddr:
                    sip=session.laddr.ip                                            #源IP
                    sport=session.laddr.port                                        #源端口
                    dip= session.raddr.ip                                           #目的IP
                    dport=session.raddr.port                                        #目的端口
                    status = session.status                                         #会话状态

                    try:
                        pid = session.pid                                           #进程号
                        exe = psutil.Process(int(pid)).name()                       #进程名
                        pid_create_time=psutil.Process(int(pid)).create_time()      #进程创建时间
                        filter_dip = netaddr.IPAddress(dip)                                 #格式化目的IP地址，用于后续判断是否是公网IP
                        filter_sip = netaddr.IPAddress(sip)
                        #数据组装
                        s = "{0:},{1:}:{2:},{3:}:{4:},{5:},{6:},{7:},{8:}".format(
                                                                                        time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                                                                                        sip,
                                                                                        sport,
                                                                                        dip,
                                                                                        dport,
                                                                                        status,
                                                                                        pid,
                                                                                        exe.lower(),
                                                                                        time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(pid_create_time)),
                                                                                        )

                        if not filter_dip.is_private() and filter_dip.is_unicast() and not filter_dip.is_link_local() and not filter_sip.is_loopback():        #判断目的IP不是私网IP，是一个单播地址，不是linklocal地址，如果符合条件就记录
                            self.record.append(s)
                    except:pass

            # return(record)

    def start(self):
        thread_collect_func = threading.Thread(target=self.collect_func,args=(True,))
        thread_collect_func.start()



    #------------根据模式做显示过滤-----------
    def filter(content,mode,exe_list=[]):
        content_list = content.split(",")
        if len(exe_list) == 1:
            if mode == "0":
                '''Running in White_list mode , no shows if don't set filter APP'''
                pass
            if mode == "1":
                return content
        elif len(exe_list) > 1:
            N2 = []
            for regex in exe_list[:-1]:
                # print(regex,'<---->',content_list[-2])                        #Debug
                N3 = re.match(regex,content_list[-2])
                if N3:
                    N2.append(content_list[-2])
            if mode == "0":
                # if content_list[-2] not in N2:
                    # print('White_list Ignore:',content_list[-2],'<--->',N2)   #Debug
                if content_list[-2] in N2:
                    return content
            elif mode == "1":
                # if content_list[-2]  in N2:
                #     print('Black_list Ignore:',content_list[-2],'<--->',N2)   #Debug
                if content_list[-2] not in N2:
                    return content


if __name__ == "__main__":

    result_store = []             #用于存放已经匹配的进程信息，用新捕获的进程与之做比较，判断新捕获的进程是否已经被捕获。

    mode = input("Run mode：\n 0 White_list\n 1 Black_list\nEnter(0 or 1): ")
    mode = Collect.input_legal_judge(mode)

    #-----------------------------循环输入进程名称---------------------
    if mode == "0":
        mode_name = "White_list"
    else: mode_name = "Black_list"
    exe_list=[]
    while 1:
        exe_list.append(input("Please input the Process name need to be put into {0:}：\n".format(mode_name)).lower())
        print(exe_list)
        if not exe_list[-1] :
            print("{1:} is in {0:}".format(mode_name,exe_list))
            break

    #-------------------table title-----------------------------------------
    print(
            "{0:^20}{1:>21}      {2:<21} {3:^11} {4:^5} {5:^19} {6:^20}".format(
                                        'Log time',
                                        'Source IP',
                                        'Dest IP',
                                        'Status',
                                        'PID',
                                        'Process Name',
                                        'Process create time',
                                        )
)

    #----------------------格式化输出-------------

    run = Collect()
    run.start()

    while True:
        for N1 in run.record:
            if N1[20:] not in result_store :
                result_store.append(N1[20:])
                info=Collect.filter(N1,mode,exe_list)
                if info == None:
                    pass
                else:
                    Log_time,Source_IP,Dest_IP,Session_Status,PID,Process_name,Process_time = info.split(",")
                    print(
                            "{0:^20}{1:>21}<---->{2:<21} {3:^11} {4:^5} {5:^19} {6:^20}".format(
                                                        Log_time,
                                                        Source_IP,
                                                        # 'Source Port',
                                                        Dest_IP,
                                                        # 'Dest Port',
                                                        Session_Status,
                                                        PID,
                                                        Process_name,
                                                        Process_time,
                                                        )
                            )


