from aip import AipSpeech
import sys
import pygame
import time
import argparse

#generator of baidu API
APP_ID = '16502526'
API_KEY = 'IW4SYMaGdrCA70Kb8H06lqrZ' 
SECRET_KEY = 'EsKZRFtCZkNydSYcdy3VAhIAEe7FaBU2'
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

#param parse

parser = argparse.ArgumentParser()
parser.add_argument('--readline',help = 'the readline context')
args = parser.parse_args()

def readline(line):
    if len(line)!= 0:
        result = client.synthesis(line,'zh',1,{'vol':5,'per':0,})
        print (line)
        if not isinstance(result,dict):
            with open('/home/pi/ok.mp3','wb') as f:
                f.write(result)
            f.close()
            print('tts success')
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/ok.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()
    
    
def tts(filename):
    f = open(filename,'r')
    command = f.read()
    if len(command) != 0:
        word = command
    f.close()
    result  = client.synthesis(word,'zh',1,{'vol':5,'per':0,})
    print (type(result))
    if not isinstance(result,dict):
        with open('/home/pi/audio.mp3','wb') as f:
            f.write(result)
        f.close()
        print('tts success')
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/audio.mp3')
    pygame.mixer.music.play()
    time.sleep(20)
    pygame.mixer.music.stop()
    
if(args.readline):
    readline(args.readline)
    
if __name__ == '__main__':
    readline('商品录入成功')

#readline("打印机已经订阅")

'''
import sys
import pygame
import time
import requests
s = time.time()
r = requests.get("http://tts.baidu.com/text2audio?lan=zh ;ie = UTF-8;spd=3;text = xcgfdsgaergdesfgrtgrt")
with open("aas.mp3","wb") as code:
    code.write(r.content)
pygame.mixer.init()
pygame.mixer.music.load("aas.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    i = 1
'''
