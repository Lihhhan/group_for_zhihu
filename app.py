#coding=utf-8
import mylog
import login
import conf
import spider
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

log = mylog.Log('./log/spider.log')

login.login()

res = {}
wordlist = {}
for person in conf.persons:
    res[person] = spider.run(person, 100)
    f = open('./data/'+person, 'w')
    log.add(person + ' downloaded!')
    for word in res[person]:
        #写入临时文件
        f.write('%s\t' % word)
        f.write('%f\n' % res[person][word])
         
        #总词数统计
        if word in wordlist:
            wordlist[word] += 1
        else:
            wordlist[word] = 1
    f.close()

#筛选重复率高和低的词
for word, count in wordlist.items():
    if float(count)/len(res) < 0.1 or float(count)/len(res) > 0.5:
        wrodlist.pop(word)

#把计数矩阵写入文件
f = open('./data/data.txt', 'w')
f.write('Word')
for word in wordlist:
    f.write('\t%s'%word)
f.write('\n')
        


for person, wc in res.items():
    f.write(person)
    for word in wordlist:
        if word in wc:
            f.write('\t%f'%wc[word]) 
        else:
            f.write('\t0')
    f.write('\n')
f.close()





