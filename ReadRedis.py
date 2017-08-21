#coding:utf8

import time
import pygame
import redis

# 1. get value by key from redis
def getData():
    r = redis.Redis(host='',password='',port=6379,db=0)
    result =  r.get('error')
    return result
#2. reference  voice  by pygame
while True:
    if getData():
        pygame.init()
        pygame.display.set_mode((200,100))
        pygame.mixer.music.load('test.mp3')
        pygame.mixer.music.play(1)
        time.sleep(10)
        pygame.mixer.music.stop()
    else:
        print'no errror!')
        time.sleep(5)