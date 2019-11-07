from fish import *
from random import randint
import matplotlib.pyplot as plt
import numpy as np

# variable de simulation
max_fish = 50
max_x = 200
max_y = 200
max_iterations = 1000
indep_fish=10

tres1 = randint(0,max_fish/2)
tres2 = randint(tres1,max_fish/2)
print(tres1)
print(tres2)


tisaa=1

interval_annim = 0.05
# functions

def dist(_x,_y):   
    x=np.asarray(_x)
    y=np.asarray(_y)
    return np.sqrt(np.sum((x-y)**2))

def center(sea):
    somme_x=0
    somme_y=0
    for fish in sea:
        somme_x += fish.x
        somme_y += fish.y
    return [somme_x/len(sea),somme_y/len(sea)]


def next(sea):
    sea_1 = sea
    sea_ret = []
    center_g = center(sea_1)
    k=0
    for fish in sea:
        if k>tres1 & k<tres2:
            fish.x+=randint(0,5)-randint(0,5)
            fish.y+=randint(0,5)-randint(0,5)
            if fish.x > max_x : fish.x = max_x
            elif fish.x < 0 : fish.x = 0
            if fish.y > max_y : fish.y = max_y
            elif fish.y < 0 : fish.y = 0
            sea_ret.append(fish)
        else :
            fish_pas = randint(10,100)
            #fish.x+=(center_g[0]-fish.x)/fish_pas
            #fish.y+=(center_g[1]-fish.y)/fish_pas
            proche_id=-1
            proche_dist=9000
            for fi in range(tres1,tres2):
                if dist([fish.x,fish.y],[sea[fi].x,sea[fi].y])<proche_dist:
                    proche_dist=dist([fish.x,fish.y],[sea[fi].x,sea[fi].y])
                    proche_id=fi
            fish.x+=(sea[proche_id].x-fish.x)/fish_pas
            fish.y+=(sea[proche_id].y-fish.y)/fish_pas
            if fish.x > max_x : fish.x = max_x
            elif fish.x < 0 : fish.x = 0
            if fish.y > max_y : fish.y = max_y
            elif fish.y < 0 : fish.y = 0
            sea_ret.append(fish)
        k+=1
        
    return sea_ret

def init_sea(sea):
    for i in range(max_fish):
        new = fish(randint(0,max_x),randint(0,max_y),sea)
        sea.append(new)


def plot_it(sea):
    for i in range(max_fish):
        if i > tres1 & i < tres2 :
            plt.plot(sea[i].x,sea[i].y,'+')
        else:
            plt.plot(sea[i].x,sea[i].y,'o')

# Progamme 

sea = []
init_sea(sea)
plt.figure(figsize=[10,15])
for k in range(max_iterations):
    plt.clf()   
    plt.xlim(-10,10+max_x)
    plt.ylim(-10,10+max_y)
    sea = next(sea)
    plot_it(sea)
    plt.pause(interval_annim)

plt.show()