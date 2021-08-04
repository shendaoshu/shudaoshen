one.py

#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Modify Author: kun zheng <shendaoshu@gmail.com>
# Modify Date:   2021-08-04 18:00
# Github URL:    https://github.com/shendaoshu
# Version:       1.0

number=25
counter=0
for i in range(10):
    counter+=1
    if counter <= 3:
        guess=int(input("Input your guess number please "))
        if guess == number:
            print("Correct")
            break
        elif guess > number:
            print("Please guess smaller")
        else:
            print("Please guess bigger")
    else:
        confirm=input("Do you want to continue. y/n")
        if confirm == "y":
            counter =0
            continue
        else:
            print("Bye")
            break