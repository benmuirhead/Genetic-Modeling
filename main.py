import turtle
import random
import math
import operator
import time

import numpy


from functions import createMember, giveShake, DNA, breedDNA, createPop, breepPop, getDNAWeights

wn = turtle.Screen()
canvaswidth = 1000
canvasheight = 1000
turtle.screensize(canvwidth=canvaswidth, canvheight=canvasheight)

turtle.setworldcoordinates(0,0,canvaswidth,canvasheight)



print(math.sqrt((450-500)**2 + (450-500)**2))

def executeBehavior(population):
    for i in range(len(population)):
        population[i].goto(population[i].xcor()+population[i].behavior[0]+population[i].giveShake()*population[i].shakeFactor
                           ,population[i].ycor()+population[i].behavior[1]+population[i].giveShake()*population[i].shakeFactor)
        population[i].weight = max(population[i].xcor() - population[i].start_x,0)
        #print(math.sqrt((population[i].xcor()-500)**2 + (population[i].ycor()-500)**2))
        if math.sqrt((population[i].xcor()-500)**2 + (population[i].ycor()-500)**2) < 150:
            population[i].obsTrip = 1

        #print(population[i].weight)
        #population[i].weight = math.sqrt((population[i].xcor()-500)**2 + (population[i].ycor()-500)**2)
        #print(population[i].weight)

def logMeanMax(dna_weights):
    a1=round(numpy.mean(dna_weights[2]),0)
    a2=round(numpy.max(dna_weights[2]),0)
    lMean.append(a1)
    lMax.append(a2)
    return(a1,a2)


def createObstacle(radius, centerX, centerY):
    obs = turtle.Turtle()
    obs.speed(0)
    obs.penup()
    obs.goto(centerX,centerY-radius)
    obs.pendown()
    obs.circle(radius)








#start area is left side of board, as a percent of canvwidth
start_area = .5

lMean=[]
lMax=[]

popSize = 20
cycles = 5
generations = 50

s = time.time()


print("round","mean","max")
for i in range(generations):
    wn.clear()
    createObstacle(150, 500, 500)
    if i==0:
        population = createPop(popSize,start_area,canvaswidth,canvasheight)
    else:
        population = breepPop(popSize, population, start_area,canvaswidth,canvasheight)
    for j in range(cycles):
        executeBehavior(population)
        # print x y for all
        if False:
            print("Population Info")
            for i in range(len(population)):
                if population[i].obsTrip == 1:
                    print(population[i].pos(),"obsTrip:", population[i].obsTrip)

    c = logMeanMax(getDNAWeights(population))
    print(i,c)
    q = getDNAWeights(population)
    #all weights
    print(q[2])
    #DNA of first two
    #print(q[0][0].__dict__)
    #print(q[0][1].__dict__)





print(lMean)
print(lMax)

e = time.time()
print("Time")
print(e-s)


#wn.bye()
wn.exitonclick()


import pylab
#pylab.__version__


pylab.plot(list(range(generations)),lMean)
#pylab.show()

pylab.plot(list(range(generations)),lMax)
#pylab.show()