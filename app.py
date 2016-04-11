#coding=utf-8
import login
import conf
import spider

login.login()

res = {}

for person in conf.persons:
     res[person] = spider.run(person, 100)



