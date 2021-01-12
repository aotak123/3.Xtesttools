import urllib.request
import ssl
import requests
import json

context = ssl._create_unverified_context()  # ssl证书免验证，python3需要验证https证书


#zhiyoo
loginurl = "http://bbs.zhiyoo.net/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"

#91wii
# urlqianzhi = "https://www.91wii.com/plugin.php?id=dc_signin:sign&infloat=yes&handlekey=sign&inajax=1&ajaxtarget=fwin_content_sign"
# urlwii = "https://www.91wii.com/plugin.php?id=dc_signin:sign&inajax=1"

# request = urllib.request.Request(urlwii)  # 构建请求url
# response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context



headers = \
  {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Origin": "http://bbs.zhiyoo.net",
    "cookie": "ikdQ_9242_connect_is_bind=1; ikdQ_9242_lastact=1607399583%09plugin.php%09; Hm_lpvt_ff27e91f286382d164f43039f143375c=1607399565; Hm_lvt_ff27e91f286382d164f43039f143375c=1606981436,1607045240; ikdQ_9242_checkpm=1; ikdQ_9242_lip=180.164.60.103%2C1607399564; ikdQ_9242_onlineusernum=978; ikdQ_9242_sendmail=1; ikdQ_9242_sid=SFz0P0; ikdQ_9242_ulastactivity=f364we2JMwB3GQxCTvjSKcsZFJs55Z8cX4LbuIExj8%2FI42J63zsl; ikdQ_9242_smile=1D1; ikdQ_9242_st_p=125767%7C1607061168%7Ce5d6c8eef67990cf6c5c3ff832281fca; ikdQ_9242_viewid=tid_70317; ikdQ_9242_forum_lastvisit=D_51_1606981676D_42_1607061165; ikdQ_9242_st_t=125767%7C1607061165%7Cc2c83b8f1cf7bf1fc6aac81f945afd37; ikdQ_9242_visitedfid=42D36D37D51; ikdQ_9242_auth=4fb9YD4dGgZKZPDpe9w10WBocD%2BZg7TqdMHvS3%2BJij3FjVJpAkZDOYIgBcxWcqjMqgwYPpMyibRHUh7LnXbURQhcbsw; ikdQ_9242_lastcheckfeed=125767%7C1607060064; ikdQ_9242_client_created=1606984150; ikdQ_9242_client_token=1403E1CABE2DF321086105E0CF81809A; ikdQ_9242_connect_login=1; ikdQ_9242_connect_uin=1403E1CABE2DF321086105E0CF81809A; ikdQ_9242_nofavfid=1; ikdQ_9242_lastvisit=1606977833; ikdQ_9242_saltkey=WO3fTXzf",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding":"gzip, deflate",
    "Host":"bbs.zhiyoo.net",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/610.2.11 (KHTML, like Gecko) Version/14.0.1 Safari/610.2.11 Maxthon/5.1.60",
    "Upgrade-Insecure-Requests":"1",
    "Referer":"http://bbs.zhiyoo.net/plugin.php?id=dsu_paulsign:sign",
    "Content-Length":"25",
    "Connection":"keep-alive"
  }
data = \
  {
    "formhash": "5f07febd",
    "qdxq": "nu"
  }
r = requests.post(loginurl,headers=headers,data=json.dumps(data))
print(r.text)