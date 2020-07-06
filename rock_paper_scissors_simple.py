# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:52:23 2020

@author: J
"""

import numpy as np
import time
print('Welcome to Rock Paper & Scissors game')
while True:
    print('Enter q to start the game or e to exit ')
    key = input()
    if key == 'q':
        i = np.random.randint(0,3)
        list = ['rock', 'paper','scissors']
        print('Ready set go.....')
        time.sleep(1)
        print(list[i])
        time.sleep(3)
    else:
        if key == 'e':
            print('Sayonara!')
            break



