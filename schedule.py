# -*- coding: utf-8 -*-

import schedule
import time




def job():
    print('do something')
    
    
    
    
def dont():
    print('dont do anything')
    
def watch():
    print('just see and watch')
    
schedule.every(3).seconds.do(job)
schedule.every().day.at('11:30').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)