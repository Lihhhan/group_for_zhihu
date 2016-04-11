#coding=utf-8
import time 

class Log:

    def __init__(self, s):
        self.lg = open(s, 'w')

    def add(self, s):
        if type(s) == str:
            print s
            t = time.strftime( '%Y-%m-%d %X', time.localtime( time.time() ) )
            self.lg.write(t + ' ' + s )

    def __del__(self):
        self.lg.close()
    

