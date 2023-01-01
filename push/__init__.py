from .workWeChat import workWechatRobot, workWechatApp
from .server import server
from .pushplus import pushplus
from .tools.dict2html import dict2html
from .tools.dict2md import dict2md
from .tools.dict2text import dict2text


def push(key, type: str, title: str, content):
    try:
        if type == "pushplus":
            try:
                res = pushplus(key).push_msg(
                    dict2html.dict2html(content),
                    title=title,
                    template="html",
                )

                print(res)
            except KeyError:
                print("未配置 pushplus 的 token")
        elif type == "server":
            try:
                res = server(key).push_msg(
                    desp=dict2md.dict2md(content),
                    title=title,
                )
            except KeyError:
                print("未配置 server 酱 的 key")
        elif type == "workWechatRobot":
            try:
                res = workWechatRobot(key).push_msg(
                    title=title,
                    content=dict2text.dict2text(content),
                )
            except KeyError:
                print("未配置微信机器人的 key")
        elif type == "workWechat":
            try:
                agentid = key["agentid"]
                corpSecret = key["corpSecret"]
                corid = key["corpid"]

                # 这里推送 text(当然也可以推送 markdown, 但是微信不支持)
                res = workWechatApp(agentid, corpSecret, corid).push_msg(
                    title=title,
                    content=dict2text.dict2text(content),
                )
            except KeyError as key:
                print(f"未配置企业微信的 {key}")
        else:
            print("未找到相关推送服务")
    except Exception as ex:
        print(f"推送时发生错误, 详情: {ex}")
