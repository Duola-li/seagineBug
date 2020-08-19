#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-08-13 15:19:07
# @Author  : Octan3 (Octan3@qq.com)
# @Link    : http://liyue.site
# @Version : 1.0
# @Function: For 

import requests
import random
import json

def main():
    num = 1
    for i in range(num):
        print(i+1,":")
        try:
            gameId, topicId = get2IDs()
        except Exception as e:
            raise e
        answerAllquestion(gameId, topicId)
        getScore(gameId, topicId)
        print("Finished one fight.\n")


def getScore(gameId, topicId):
    URL = "https://topic.seagine.com/feihualing/api/online/submit_result"
    params = {"topicId":topicId,
        "gameId":gameId}
    UID = "5f3247795127234ff0578ab2"   #我的
    # UID = "5f3245115127234ff0578a64"   #马晓敏
    r = requests_post(URL, UID, params=params)
    # try:
    #     rd = json.loads( r.text )
    #     print()
    # except Exception as e:
    #     print("result json decode error")
    #     print(r.text)
    print(r.text)

def getIDs2():
    #获取gameID和topicId，根据随机的UID
    #UID： 5f3247795127234ff0578ab2
    # ?    5f32477951272382d34abec5
    n = 10
    orgin = "5f3247795127234ff0578ab2"
    idsss = "0123456789abcdef"
    # tempUID = orgin[:-n] + ''.join(random.sample(idsss, n))
    tempUID = "5f3247795127234ff0578ab2"   #我的
    print("fakeID:", tempUID)
    URL = "https://topic.seagine.com/feihualing/api/online/start"
    topicId = "5f31149cafaa520c46795441"
    params = {"topicId":topicId,"tagId":"5f31112fafaa520c467947fb","refererid":"5f3245115127234ff0578a64","levelCode":"b"}
    r = requests_post(URL, tempUID, params)
    text = r.text
    try:
        myr = json.loads(text)
        gameId = myr['data']['gameId']
    except Exception as e:
        print("id used. continue")
        print(text)
        raise e
    print( "Get id Success:", gameId)
    return gameId, topicId

def get2IDs():
    print("get2IDs")
    #获取gameID和topicId，根据随机的UID
    #UID： 5f3247795127234ff0578ab2
    # ?    5f32477951272382d34abec5
    n = 2
    orgin = list( "5f3247795127234ff0578ab2" )
    idsss = "0123456789abcdef"
    for i in range(n):
        orgin[random.randint(0, 23)] = idsss[random.randint(0, 15)]
    tempUID = "".join(orgin)
    print("fakeID:", tempUID)
    URL = "https://topic.seagine.com/feihualing/api/online/start"
    topicId = "5f31149cafaa520c46795441"
    params = {"topicId":topicId,"tagId":"5f31112fafaa520c467947fb","refererid":"5f3245115127234ff0578a64","levelCode":"b"}
    r = requests_post(URL, tempUID, params)
    text = r.text
    try:
        myr = json.loads(text)
        gameId = myr['data']['gameId']
    except Exception as e:
        print("id used. continue")
        print(text)
        raise e
    print( "Get id Success:", gameId)
    return gameId, topicId
    

def answerAllquestion(gameId, topicId):
    #对game回答问题，获取game分数
    qa = {
        "5f31112fafaa520c46794838":0,
        "5f31112fafaa520c4679485c":1,
        "5f31112fafaa520c4679484f":0,
        "5f31112fafaa520c46794831":3,
        "5f31112fafaa520c46794834":2,
        "5f31112fafaa520c46794851":0,
        "5f31112fafaa520c4679483d":0,
        "5f31112fafaa520c46794833":2,
    }
    for i in qa.keys():
        postAnswer(gameId, topicId, qa[i], i)
    print("answerAllquestion, Done")

def postAnswer(gameId, topicId, option, questionId):
    # 5f3247795127234ff0578ab2  
    params = {"topicId":topicId,
        "gameId":gameId,
        "option":option,
        "time":2.338,
        "questionId":questionId}

    URL = "https://topic.seagine.com/feihualing/api/online/answer"
    r = requests_post(URL, params=params)
    print( r.text )

def postAnswer2(gameId, topicId, option, questionId):
    headers = {
            # X-Requested-With: com.tencent.mm
            # Sec-Fetch-Site: same-origin
            "Origin": "https://topic.seagine.com",
            'User-Agent': 'Mozilla/5.0 (Linux; Android 9; AQM-AL10 Build/HONORAQM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045318 Mobile Safari/537.36 MMWEBID/2400 MicroMessenger/7.0.13.1640(0x27000D38) Process/tools NetType/WIFI Language/zh_CN ABI/arm64 WeChat/arm32',
            'Cookie': 'Hm_lvt_0e8ee093e255598142658b4d322e85d6=1596589937; gallop_userid=5f3247795127234ff0578ab2; gallop_avatar=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJ3huEe5FianSIv7nnib9KmeRVvqT0T5j9D8qSOwibKwxb7tO8OsuNGu8WayF9T1C3wP1KgvuDqiaGclA%2F132; gallop_nickname=%E6%9D%8E%E9%98%85_OUC_CS_CA; _ga=GA1.2.60700901.1597295120; _gid=GA1.2.889547938.1597295120; Hm_lpvt_0e8ee093e255598142658b4d322e85d6=1597297017'
        }
    params = {"topicId":topicId,
        "gameId":gameId,
        "option":option,
        "time":2.338,
        "questionId":questionId}
    r = requests.post("https://topic.seagine.com/feihualing/api/online/answer", data=params)
    print( r.text )

# def requests_post(URL, UID="5f3247795127234ff0578ab2" ,params={}):
def requests_post(URL, UID="5f3247795127234ff0578ab2" ,params={}):    
    # UID:5f3247795127234ff0578ab2 我的
    headers = {
            # X-Requested-With: com.tencent.mm
            # Sec-Fetch-Site: same-origin
            "Origin": "https://topic.seagine.com",
            'User-Agent': 'Mozilla/5.0 (Linux; Android 9; AQM-AL10 Build/HONORAQM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045318 Mobile Safari/537.36 MMWEBID/2400 MicroMessenger/7.0.13.1640(0x27000D38) Process/tools NetType/WIFI Language/zh_CN ABI/arm64 WeChat/arm32',
            'Cookie': 'Hm_lvt_0e8ee093e255598142658b4d322e85d6=1596589937; gallop_userid='+ UID +'; gallop_avatar=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJ3huEe5FianSIv7nnib9KmeRVvqT0T5j9D8qSOwibKwxb7tO8OsuNGu8WayF9T1C3wP1KgvuDqiaGclA%2F132; gallop_nickname=%E6%9D%8E%E9%98%85_OUC_CS_CA; _ga=GA1.2.60700901.1597295120; _gid=GA1.2.889547938.1597295120; Hm_lpvt_0e8ee093e255598142658b4d322e85d6=1597297017'
        }
    # print(headers['Cookie'])
    print(UID)
    r = requests.post(URL, headers=headers, data=params)
    return r

if __name__ == '__main__':
    main()

