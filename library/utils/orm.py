from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os

# print(os.getcwd())
Base = declarative_base()


class Poc(Base):
    """
    name 为poc名字
    shell_type 为poc类型,分三种,
        2,可以获取shell
        1, 可以获取webshell
        0, 只能get flag
    os_type
        0 php
        1 python
    """
    __tablename__ = 'poc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    shell_type = Column(Integer)
    os_type = Column(Integer)


class Target(Base):
    """
    用于对要攻击的主机管理
    ip 为对方ip
    s_reach  是否可以访问
    is_get_shell   是否已经获取到了shell
    flag  获取的flag
    flag_create_time  获取的flag时间
    """
    __tablename__ = 'target'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30))
    is_reach = Column(Boolean)
    is_get_shell = Column(Boolean)
    flag = Column(String(50))
    flag_create_time = Column(DateTime)


class Message(Base):
    """
    用于对流量信息的记录
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, autoincrement=True)
     http内容
    message = Column(Text)
    请求类型,get还是post
    http_type = Column(Integer)
    请求的server主机
    host = Column(String(30))
    来源ip
    source_ip = Column(String(30))
    请求时间
    create_time = Column(DateTime)

    """
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(Text)
    http_type = Column(Integer)
    server = Column(String(30))
    source_ip = Column(String(30))
    create_time = Column(DateTime)


def database_init(game_name='test'):
    # 　先使用内存数据库,
    # engine = create_engine('sqlite://')
    # engine = create_engine(
    #     'sqlite:///../../games/' + game_name + '/data.sqlite3')
    engine = create_engine(
        'sqlite:///games/' + game_name + '/data.sqlite3')
    Base.metadata.create_all(engine)
    # 返回数据库操操作对象Session
    return sessionmaker(bind=engine)

if __name__ == '__main__':

    Session = database_init('test')

    session = Session()
    ed_poc = Poc(name='a', shell_type=0, os_type=0)
    ed_target = Target(ip="127.0.0.1", is_get_shell=False)
    session.add(ed_poc)
    session.add(ed_target)
    session.commit()


