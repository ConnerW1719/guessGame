#!/usr/bin/env python3
#Guess Game
#Conner Walkenhorst
#10/30/2017
#Simple number guessing game

from random import randint

MIN = 1
MAX = 20

targetNumber = randint(MIN, MAX)
print(targetNumber)