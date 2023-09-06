import random
import time
import numpy as np
import Rabbit
import Alligator
import Python
import LineGraph as LG
import Matrix as M

random.seed(time.time()) #calculates a randome time
EMPTY = [] #creates an empty list called EMPTY
RABBIT = [] #creates an empty list called RABBIT
ALLIGATOR = [] #creates an empty list called ALLIGATOR
PYTHON = [] #creates an empty list called PYTHON
TIME = [] #creates an empty list called TIME
A = [[random.randint(0, 2) for x in range(30)] for y in range(30)] #calculates a random integer between 0 and 2 for each spot in the 30 x 30 matrix
empty, rabbit3, alligator3 = 0, 0, 0 #assigns 0 as the value for the empty, rabbit3, and alligator3 variables
for x in range(0, 30): #for loop that loops through each row of the matrix
    for y in range(0, 30): #nested for loop that loops through each column of each row
        if A[x][y] == 0: #checks if there is an animal at the given position of the matrix
            empty += 1 #adds 1 to the value of the empty variable
        elif A[x][y] == 1: #checks if the animal at the given position of the matrix is a rabbit
            rabbit3 += 1 #adds 1 to the value of the rabbit3 variable
        elif A[x][y] == 2: #checks if the animal at the given position of the matrix is an alligator
            alligator3 += 1 #adds 1 to the value of the alligator3 variable

count1 = 0 #sets the value of the count1 variable equal to 0

while count1 <= 19: #while loop that continues as long as the value of the count1 variable is less than or equal to 19
    for x in range(0, 29): #nested for loop that loops through each row of the matrix
        for y in range(0, 29): #nested for loop that loops through each column of the xth row of the matrix
            if A[x][y] == 0: #checks if the value at the given position of the matrix is equal to 0
                continue #continues with the loop
            elif A[x][y] == 1: #checks if the value at the given position of the matrix is equal to 1
                Rabbit.rabbit(x,y,A)#calls to the rabbit function of the Rabbit class and passes the necessary parameters
            elif A[x][y] == 2: #checks if the value at the given position of the matrix is equal to 2
                Alligator.alligator(x,y,A)#calls to the alligator function of the Alligator class and passes the necessary parameters

    empty, rabbit2,alligator2 = 0,0,0 #assigns 0 as the value for the empty, rabbit2, and alligator2 variables
    for x in range(0,30): #for loop that loops through each row of the matrix
        for y in range(0,30): #nested for loop that loops through each column of the xth row of the matrix
            if A[x][y] == 0: #checks if the value at the given position of the matrix is equal to 0
                empty +=1 #adds 1 to the value of the empty variable
            elif A[x][y] == 1: #checks if the value at the given position of the matrix is equal to 1
                rabbit2 += 1 #adds 1 to the value of the rabbit2 variable
            elif A[x][y] == 2: #checks if the value at the given position of the matrix is equal to 2
                alligator2 += 1 #adds 1 to the value of the alligator2 variable
    EMPTY.append(empty)#adds the empty variable to the EMPTY list
    RABBIT.append(rabbit2)#adds the rabbit2 variable to the RABBIT list
    ALLIGATOR.append(alligator2)#adds the alligator2 variable to the ALLIGATOR list
    TIME.append(6*count1)#adds 6*the count1 variable to the TIME list
    M.matrix(A, count1)
    count1 += 1 #adds 1 to the value of the count1 variable
LG.plotDynamics(RABBIT,ALLIGATOR,TIME)#plots the RABBIT, ALLIGATOR, and TIME lists

count2 = 0 #sets the value of the count2 variable equal to 2
for x in range(0,29): #for loop that loops through each row of the matrix
    for y in range (0,29): #nested for loop that loops through each column of the xth row of the matrix
        if A[x][y] == 0: #checks if the value at the given position of the matrix is equal to 0
            A[x][y] = 3 #sets the value at the given position of the matrix equal to 3
            count2 += 1#adds 1 to the value of the count2 variable
            if count2 == 5:#checks if the value of the count2 variable is equal to 5
                break#ends the current iteration of the loop
        else:
            continue#continues the current iteration of the loop
    if count2 == 5:#checks if the value of the count2 variable equals 5
        break#ends the current iteration of the loop

M.matrix(A,20)
empty2, rabbit3,alligator3,python = 0,0,0,0#sets the intial values of the empty2, rabbit3, alligator3, and python variables equa to 0
for x in range(0,30):#for loop that loops through each row of the matrix
    for y in range(0,30):#nested for loop that loops through each column of each row
        if A[x][y] == 0:#checks if the value at the given position of the matrix equals 0
            empty2 +=1#adds 1 to the empty2 variable
        elif A[x][y] == 1:#checks if the value at the given position of the matrix equals 1
            rabbit3 += 1#adds 1 to the rabbit3 variable
        elif A[x][y] == 2:#checks if the value at the given position of the matrix equals 2
            alligator3 += 1#adds 1 to the alligator3 variable
        elif A[x][y] == 3:#checks if the value at the given position of the matrix equals 3
            python += 1#adds 1 to the python variable

EMPTY1 = []#creates an empty list called EMPTY1
RABBIT1 = []#creates an empty list called RABBIT1
ALLIGATOR1 = []#creates an empty list called ALLIGATOR1
PYTHON1 = []#creates an empty list called PYTHON1
TIME1 = []#creates an empty list called TIME1
count3 = 0#sets the value of the count3 variable equal to 0
while count3 <= 100:#while loop that continues as long as the value of the count3 variable is less than or equal to 100
    for x in range(0, 29):#nested for loop that loops through each row of the matrix
        for y in range(0, 29):#nested for loop that loops through each column of the xth row of the matrix
            if A[x][y] == 0:#checks if the value at the given position of the matrix equals 0
                continue#continues with the current iteration of the loop
            elif A[x][y] == 1:#checks if the value at the given position of the matrix equals 1
                Rabbit.rabbit(x,y,A)#calls to the rabbit function of the Rabbit class and passes the necessary parameters
            elif A[x][y] == 2:#checks if the value at the given position of the matrix equals 2
                Alligator.alligator(x,y,A)#calls to the alligator function of the Alligator class and passes the necessary parameters
            elif A[x][y] == 3:#checks if the value at the given position of the matrix equals 3
                Python.python(x,y,A)#calls to the python function of the Python class and passes the necessary parameters

    empty, rabbit3,alligator3, python1 = 0,0,0,0#assigns 0 as the value for the empty, rabbit3, and alligator3 variables
    for x in range(0,30):#for loop that loops through each row of the matrix
        for y in range(0,30):#nested for loop that loops through each column of each row
            if A[x][y] == 0:#checks if the value at the given position of the matrix equals 0
                empty +=1#adds 1 to the empty variable
            elif A[x][y] == 1:#checks if the value at the given position of the matrix equals 1
                rabbit3 += 1#adds 1 to the rabbit3 variable
            elif A[x][y] == 2:#checks if the value at the given position of the matrix equals 2
                alligator3 += 1#adds 1 to the alligator3 variable
            elif A[x][y] == 3:#checks if the value at the given position of the matrix equals 3
                python1 += 1#adds 1 to the python1 variable

    EMPTY1.append(empty)#adds the empty variable to the EMPTY1 list
    RABBIT1.append(rabbit3)#adds the rabbit3 variable to the RABBIT1 list
    ALLIGATOR1.append(alligator3)#adds the alligator3 variable to the ALLIGATOR1 list
    TIME1.append((6*count3) +114)#adds the 6*the count3 variable to the TIME1 list
    PYTHON1.append(python1)#adds the python1 variable to the PYTHON1 list
    M.matrix(A,count3+21)
    count3 += 1#adds 1 to the value of the count3 variable
LG.plotDynamics1(RABBIT1,ALLIGATOR1,PYTHON1,TIME1)#plots the RABBIT1, ALLIGATOR1, PYTHON1, and TIME1 lists





















