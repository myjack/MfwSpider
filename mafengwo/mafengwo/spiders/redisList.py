#!/usr/bin/python
#coding=utf-8


import redis

class urlList():

#############################################
# create by myjack                          #
# you can call the function by urlList Class#
# vertion : v-01                            #
# date : 2015-4-5                           #
#############################################

    def __init__(self):
        self.pool    = redis.ConnectionPool(host='localhost', port=6379, db=0)
        self.Redis   = redis.Redis(connection_pool = self.pool)

    # push a new link at the end of list
    def lpushLink(self,rlist,value):
        return self.Redis.lpush(rlist,value)

    #return the last link
    def lpopLink(self,rlist,value):
        return self.Redis.lpop(rlist)

    #return the first link
    def rpopLink(self,rlist,value):
        return self.Redis.rpop(rlist)

    #get length of list
    def lenList(self,rlist):
        return self.Redis.llen(rlist)

    #init list 
    def delList(self,rlist):
        return self.Redis.delete(rlist)
