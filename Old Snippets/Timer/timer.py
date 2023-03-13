# -*- coding: utf-8 -*-
"""
Created on Sat Aug  18 13:29:12 2018

@author: Avis_King
"""

import time

print('Press ENTER to begin, Press Ctrl + C to stop')

while True:
    try:
        input() 
        starttime = time.time()
        print('Started')
    except KeyboardInterrupt:
        print('Stopped')
        endtime = time.time()
        print('Total Time:', round(endtime - starttime, 2),'secs')
        break