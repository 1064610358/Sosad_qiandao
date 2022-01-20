import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]

# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]

# 填入账号对应cookie
cookie = os.environ["COOKIE"]


def start():    
    url= "https://www.xn--pxtr7m5ny.com/qiandao"
    referer = 'https://www.xn--pxtr7m5ny.com/'
    #checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    origin = "https://www.xn--pxtr7m5ny.com/"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"
    payload={
        'token': 'xn--pxtr7m5ny_network'
    }
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
   # print(res)
 
if sever == 'on':
       requests.get('sctapi.ftqq.com/'+sckey+'.send?text='ok')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()

    
