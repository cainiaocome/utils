#!/usr/bin/env python2.7
# encoding: utf-8

import requests
import json
import threading

from config import lianzhong_username, lianzhong_password, lianzhong_key

def check_point():
    url = 'http://bbb4.hyslt.com/api.php?mod=php&act=point'
    r = requests.post(url=url, data={'user_name':lianzhong_username, 'user_pw':lianzhong_password})
    return json.loads(r.text)
    # return format:
    # {
    # 	"result": bool,
    #   "data": (id, val) # id为验证码id，val为结果，如果失败data返回失败原因
    # }

def report_error(yzm_id):
    url = 'http://bbb4.hyslt.com/api.php?mod=php&act=error'
    r = requests.post(url=url, data={'user_name':lianzhong_username, 'user_pw':lianzhong_password, 'yzm_id':str(yzm_id)})
    return json.loads(r.text)
    # return format:
    # {
    # 	"result": bool,
    # }

def de_captcha(captcha='captcha.png'):
    url = 'http://bbb4.hyslt.com/api.php?mod=php&act=upload'
    files = {'upload':open(captcha, 'rb')}
    r = requests.post(url=url, data={'user_name':lianzhong_username, 'user_pw':lianzhong_password, 'yzm_minlen':5,
        'yzm_maxlen':5, 'yzmtype_mark':25, 'zztool_token':'phrack'}, files=files)
    return json.loads(r.text)
    # return format:
    # {
    # 	"result": bool,
    #   "data": int(success) or str(failure)
    # }

if __name__=='__main__':
    print check_point()
