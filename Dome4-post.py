# -*- coding:utf-8 -*-
import urllib
import urllib2
# http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With" : "XMLHttpRequest",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    }
trans_info = raw_input("请输入你要翻译的文字")
data_format = {
    "i": trans_info,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",

    "sign": "d2bad9c474f0bdca1281ab7c7438f30e",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
    "typoResult": "false"
}
data = urllib.urlencode(data_format)
# print data
request = urllib2.Request(url, data=data,headers=headers)
content = urllib2.urlopen(request).read()

print(content.decode("utf-8"))