class FrameworkRuntimeException(Exception):
    """
    框架运行时出错，将会抛出此异常
    如 运行是缺少必须文件等

    """

    def __init__(self, msg):
        super(FrameworkRuntimeException, self).__init__(msg)
        self.msg = msg
