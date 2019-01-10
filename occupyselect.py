# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:00:29 2019

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

program framework for description and simulation of occupation selection, capacity, and earnings

Suggested citation as computer software for reference:
Pan, Alan J. (2019). Occupation Selection [Computer software]. Github repository <https://github.com/alanjpan/Occupation-Selection>

Note this software's license is GNU GPLv3.
"""

import math
import random

selection = [0, 62, 93]
occupations = ['A', 'B', 'C']
capacity = [100, 50, 10]
training = [1, 5, 10]
earnings = [20, 40, 60]

employees = [0, 0, 0]
agent_occupation = []
agent_training = []
agent_earnings = []

for loop in range(160):
    select = random.randrange(0, 100, 1)
    for i in range(len(selection)-1, -1, -1):
        if select > selection[i]:
            if capacity[i] > employees[i]:
                agent_occupation.append(occupations[i])
                agent_training.append(0)
                agent_earnings.append(0)
                employees[i] += 1
                break
            else:
                loop -= 1

print(employees)

def printresults():
    A_earnings = 0
    B_earnings = 0
    C_earnings = 0
    for i in range(len(agent_occupation)):
        if agent_occupation[i] == 'A':
            A_earnings += agent_earnings[i]
        elif agent_occupation[i] == 'B':
            B_earnings += agent_earnings[i]
        elif agent_occupation[i] == 'C':
            C_earnings += agent_earnings[i]
    print('after ' + str(year) + ' years...')
    print('total earnings A: ' + str(A_earnings))
    print('average earnings A: ' + str(int(A_earnings/employees[0])))
    print('total earnings B: ' + str(B_earnings))
    print('average earnings B: ' + str(int(B_earnings/employees[1])))
    print('total earnings C: ' + str(C_earnings))
    print('average earnings C: ' + str(int(C_earnings/employees[2])))
    print()

print()
year = 0
while year < 80:
    for i in range(len(agent_occupation)):
        job = occupations.index(agent_occupation[i])
        if agent_training[i] > training[job]:
            agent_earnings[i] += earnings[job]
        else:
            agent_training[i] += 1
    year += 1

    if year == 10:
        printresults()
    elif year == 20:
        printresults()
    elif year == 30:
        printresults()
    elif year == 40:
        printresults()
    elif year == 50:
        printresults()
    elif year == 60:
        printresults()
    elif year == 70:
        printresults()
    elif year == 80:
        printresults()
