# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import urllib
import urllib2
import cookielib
import json
url = 'http://biz.o3cloud.cn/app/admin/order/admin_order_list_view'
# url = 'https://aoao-dev-admin.o3cloud.cn'

account = '666666'
verify_code = '693345'

# content = urllib2.urlopen('http://biz.o3cloud.cn/app/admin/order/admin_order_list_view')
# print content.read(),"13"

#使用代理服务器
# proxy_support = urllib2.ProxyHandler({'http':'http://61.135.169.121:8080'})
# opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
# urllib2.install_opener(opener)
# content = urllib2.urlopen(url).read()
# print content,"19"

#需要登录的情况
cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)
content = urllib2.urlopen(url).read()
# print content,"27"

#表单的处理
postdata = urllib.urlencode({
    'account': account,
    'verify_code': verify_code
})

req = urllib2.Request(
    url = url,
    data = postdata
)
result = urllib2.urlopen(req).read()
# print result,"43"

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

req = urllib2.Request(
    url = url,
    data=postdata,
    headers = headers
)
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]
urllib2.install_opener(opener)
response = urllib2.urlopen(url)
print req.type,"52",type(req),response

def login():
    data = urllib.urlencode(
        {
            'account': account,
            'verify_code': verify_code,
            'continue':'http://biz.o3cloud.cn/app/admin/order/admin_order_list_view',
            'save_cookie':1
        }
    )
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read().decode('utf-8')


# 创建一个OpenerDirector的实例，传入一个CookieJar的Handler，用于自动处理cookie
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# loginparams = {'account':account,
#                'verify_code':verify_code
#                }

# 向opener中addheaders，之后用这个opener提交的request都会自动加入这些首部字段
# headers = {'User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# req = urllib2.Request(url,urllib.urlencode(loginparams),headers=headers)
# response = urllib2.urlopen(req)
# operate = opener.open(req)
# thepage = response.read()
# print thepage

# opener.add_handler = [
#     ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'),
#     ()
# ]