#coding=utf-8
import urllib
import urllib2
import cookielib
import json

"cookie init"
cookies = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
urllib2.install_opener(opener)

c =  urllib2.urlopen('http://www.zhihu.com')


def login():
    "login"
    form =  {}
    for cookie in cookies:
        if cookie.name == '_xsrf' :
            form['_xsrf'] = cookie.value
    form['password'] = 'qwe383548557'
    form['email'] = '136081054@qq.com'
    form['remember_me'] = False

    post_data=urllib.urlencode(form)
    headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
    req=urllib2.Request('https://www.zhihu.com/login/email',post_data,headers)
    content=json.load(opener.open(req))

    if content['r'] == 0 :
        print content['msg']
    else: 
        if data in content: 
            print content['data']    
            exit()


