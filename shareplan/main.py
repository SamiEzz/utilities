import matplotlib.pyplot as plt
import numpy as np
from random import randrange
#####################
#    Functions      #
#####################


def getY(x):
    y = []
    entryValue = 37
    randRg = 3
    xOffset1 = 8
    xOffset2 = 16
    xOffset3 = 24
    yMultip1 = 1
    yMultip2 = 1.4
    yMultip3 = 1.8
    yMultip4 = 2.2

    for i in range(len(x)):
        if(x[i] < xOffset1):
            y.append(entryValue*yMultip1*(1+randrange(-randRg, randRg)*0.05))
        elif(xOffset1 <= x[i] and x[i] < xOffset2):
            y.append(entryValue*yMultip2*(1+randrange(-randRg, randRg)*0.05))
        elif(xOffset2 <= x[i] and x[i] < xOffset3):
            y.append(entryValue*yMultip3*(1+randrange(-randRg, randRg)*0.05))
        else:
            y.append(entryValue*yMultip4*(1+randrange(-randRg, randRg)*0.05))
    return y


def calculateSum(y):
    sum = 0
    for i in y:
        sum += i
    return sum


def calculateStock(y, entrySum):
    stock = 0
    nbOfActions = 0
    for elem in y:
        nbOfActions += entrySum/elem
    stock = nbOfActions*y[-1]
    return stock
#####################
#  prepare vectors  #
#####################


x = np.linspace(1, 24, 24)
y = getY(x)
sum = calculateSum(y)
stock = calculateStock(y, 250)

#####################
#       Plot        #
#####################
plt.plot(x, y)
plt.text(x[-1], y[-1], str(stock))
plt.show()
