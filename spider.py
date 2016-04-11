#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import jieba

def run(name, number):
    i = 0
    wordcount = { }
    while i < number/20 :
        i = i + 1
        #数据抓取
        url = 'http://www.zhihu.com/people/' + name + '/answers?page=' + str(i) 
        print url
        req = urllib2.Request(url)
        req.add_header("User-agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36")
        c = urllib2.urlopen(req)

        #数据处理
        content = BeautifulSoup(c.read())
        answers = content.find(id = "zh-profile-answer-list")

        answer = answers.div
        while True:
            #被折叠的回答～
            if answer.textarea != None:
                tag_as = answer.find_all('a')
                for a in tag_as: 
                    if a['class'] == 'question_link' or a['class'] == 'zm-item-vote-count js-expand js-vote-count':
                        print a.string
                print answer.textarea.get_text()
            
            answer = answer.next_sibling.next_sibling
            if answer == None:
                break




