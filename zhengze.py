#coding:utf-8
import requests,re
url="http://search.jd.com/Search?keyword=iphone6&enc=utf-8"
resp=requests.get(url)
print re.findall("已有(\d+)人评价",resp.content,re.S)