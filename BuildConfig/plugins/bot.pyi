class Logger:
    def info(*msg):
        """输出INFO信息"""
        ...
    def debug(*msg):
        """输出DEBUG调试信息"""
        ...
    def error(*msg):
        """输出Error错误信息"""
        ...
    def warn(*msg):
        """输出Warn警告信息"""
        ...

def getVersion() -> str:
    """获取Bot版本字符串"""
    ...

def runCommand(cmd:str) -> bool:
    """
    向服务端发送命令
    
    :param cmd: 命令
    """
    ...

def sendGroupMsg(group:str,msg:str):
    """
    向指定的群发送消息
    
    :param group: 群聊
    :param msg: 消息
    """
    ...

def sendAllGroupMsg(msg:str):
    """
    向所有群发送消息
    
    :param msg: 消息
    """
    ...

def recallMsg(target:str):
    """
    撤回消息
    
    :param target: 消息Target
    """
    ...

def sendApp(group:str,code:str):
    """
    向指定的群发送APP消息
    
    :param group: 群聊
    :param code: APP Code
    """
    ...

def sendPacket(packet:str):
    """
    向Mirai发送自定义包
    
    :param cmd: 命令
    """
    ...

def setListener(event: str, function: callable[[dict], None]) -> bool:
    """
    设置监听器(监听器可前往:https://cspbot.top/#/zh-cn/开发文档/API文档 查看)

    :param event: 监听器名称
    :param function: 回调函数
    """
    ...

def registerCommand(cmd: str, function: callable[[list[str]], None]) -> bool:
    """
    注册指令（可以免去正则前的<<）

    :param cmd: 监听器名称
    :param function: 回调函数
    """
    ...


def getAllAPIList()->list[str]:
    """
    获取所有API列表
    """
    ...

def tip(type:str,title:str,content:str,options:list[str]) -> str:
    """
    提示框
    
    :param type: 提示类型
    :param title: 提示标题
    :param content: 提示内容
    :param options: 窗口按钮
    """
    ...

def motdbe(ip_port:str) -> str:
    """
    获取BE的Motd信息
    
    :param ip_port: 地址及端口 例:127.0.0.1:19132
    """
    ...

def motdje(ip_port:str) -> str:
    """
    获取JE的Motd信息
    
    :param ip_port: 地址及端口 例:127.0.0.1:25565
    """
    ...

def getAPIVersion() -> int:
    """
    获取API版本
    """
    ...

def getGroup() -> list[str]:
    """
    获取管理的群
    """
    ...

def getAdmin() -> list[str]:
    """
    获取管理员
    """
    ...

def bind(name:str,qq:str) -> bool:
    """
    绑定Xbox
    
    :param name: 用户名
    :param qq: QQ号
    """
    ...

def unbind(qq:str) -> bool:
    """
    解绑Xbox
    
    :param qq: QQ号
    """
    ...

def queryData(type:str,key:str) -> dict:
    """
    查询Xboxid
    
    :param type: 数据类型(qq,xuid,player)
    :param key: 查询键
    注:没有返回空Dict:{}
    """
    ...

def getServerStatus() -> bool:
    """
    获取服务器状态
    """
    ...