#coding:utf-8
'''
Created on 2017年6月27日

@author: Administrator
'''
import urllib.request
import re
import time
import urllib.error
#设置使用代理服务器爬取
def use_proxy(proxy_addr,url):
    import urllib.request
    try:
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
        proxy = urllib.request.ProxyHandler(proxy_addr)
        opener = urllib.request.build_opener()
        opener.addheaders=[headers]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print('Exception:'+str(e))
        time.sleep(1)
#获取搜索页面的url
urllist =[]
def geturllist(key,pagestart,pageend,proxy):
    
        