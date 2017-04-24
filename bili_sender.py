#!/usr/bin/python
#coding=utf-8
import requests
import json
import time 

SEND_URL = 'http://live.bilibili.com/msg/send'
TV_URL = 'http://api.live.bilibili.com/SmallTV/join'

class Sender(object):

    def __init__(self, cookies):
        self.cookies = cookies

    def sendDanmaku(self, roomid, content, color='white'):
        content = content.strip()
        if not content: return
        if color == 'white': color = 16777215;
        elif color == 'blue': color = 6737151;
        params = {
            "color":color, #16777215-white, #6737151-blue
            "fontsize":25,
            "mode":1,
            "msg":content,
            "rnd":int(time.time()),
            "roomid":roomid
            }
        r = requests.post(SEND_URL, data=params, cookies=self.cookies)
        result = r.content
        raw = json.loads(result)
        if raw['code'] != 0: print raw['msg']
    
    def joinSmallTV(self, roomid, tv_id):
        params = {
                'roomid':roomid,
                'id':tv_id,
                '_':int(time.time() * 100)
                }
        r = requests.get(TV_URL, params=params, cookies=cookies)
        result = r.content
        raw = json.loads(result)
        if raw['code'] != 0: print raw['msg']

if __name__ == '__main__':
    import bili_config
    config = bili_config.Config('config.txt')
    sender = Sender(config.cookies)
    while 1:
        content = raw_input()
        sender.sendDanmaku(90012, content)
