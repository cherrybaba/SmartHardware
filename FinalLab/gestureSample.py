import requests
import base64

'''
手势识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture"
# 二进制方式打开图片文件
f = open('[本地文件]', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())

'''
 {
        "log_id": 4466502370458351471,
        "result_num": 2,
        "result": [{
            "probability": 0.9844077229499817,
            "top": 20,
            "height": 156,
            "classname": "Face",
            "width": 116,
            "left": 173
        },
        {
            "probability": 0.4679304957389832,
            "top": 157,
            "height": 106,
            "classname": "Heart_2",
            "width": 177,
            "left": 183
        }]
    }
'''