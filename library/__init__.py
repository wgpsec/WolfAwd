import sys

from .utils.error import *
from importlib import import_module


def run(global_config):
    try:
        """
        动态拼接运行模式cli ，将 通用视图导入，包含比赛初始化页面
        """
        mode = global_config["mode"]
        default_type = global_config["default_type"]
        common_views = import_module("library.views.common."+mode)
    except KeyError:
        raise FrameworkRuntimeException("global_config 内容缺失")
    except ModuleNotFoundError:
        raise FrameworkRuntimeException("mode default_type 配置错误，模块未找到")

    common_views.show()
    """
    蒋games文件夹加入搜索路径,导入
    game.config  是games 目录的配置信息,包含当前比赛名称
    利用当前比赛明确获取 current_game_config
    从 current_game_config 获取 type

    """
    sys.path.append("../games")
    import games
    current_game = import_module("games."+games.config["now_game"])
    current_game_config = current_game.config
    #　如果用户未指定，type类型,既攻击还是防守,使用框架默认配置
    current_type = current_game_config.get('type', default_type)
    """
     实现视图的切换,
     攻击和防护模块show函数应该返回希望切换的模块,defense 或者 exploit
     如果返回为空,则结束框架执行
     
    """
    while current_type:
        type_views = import_module("library.views."+current_type+"."+mode)
        current_type = type_views.show()
    """
    结束视图
    """
    common_views.exit()
