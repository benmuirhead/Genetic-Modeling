import turtle
import random
import math
import operator
import time

import numpy


wn = turtle.Screen()
canvaswidth = 1000
canvasheight = 1000
turtle.screensize(canvwidth=canvaswidth, canvheight=canvasheight)

turtle.setworldcoordinates(0,0,canvaswidth,canvasheight)



#print("hello")


def createMember(start_area,bredDNA):
    member = turtle.Turtle()
    member.start_x = random.randint(0,canvaswidth*start_area)
    member.start_y = random.randint(0,canvasheight)
    member.speed(0)
    member.penup()
    member.goto(member.start_x,member.start_y)

    member.dna = bredDNA
    member.behavior = [member.dna.xMove,member.dna.yMove]
    member.shakeFactor = member.dna.shake

    member.giveShake = giveShake
    member.weight=0
    return member



def giveShake():
    return random.randint(-20,20)




class DNA:
    def __init__(self):
        self.shake = random.randint(0, 2)
        self.xMove = random.randint(0, 20)
        self.yMove = random.randint(-10, 10)



dna3 = DNA()
#a = createMember(.4,dna3)


def breedDNA(dna1,dna2):
    newDNA = DNA()

    if random.randint(0,1) ==0:
        newDNA.shake = dna1.shake
    else:
        newDNA.shake = dna2.shake

    if random.randint(0,1) ==0:
        newDNA.xMove = dna1.xMove
    else:
        newDNA.xMove = dna2.xMove

    if random.randint(0,1) ==0:
        newDNA.yMove = dna1.yMove
    else:
        newDNA.yMove = dna2.yMove

    return newDNA



#start area is left side of board, as a percent of canvwidth
start_area = .3

def createPop(count):
    population = []
    for i in range(count):
        createdDNA = DNA()
        population.append(createMember(start_area,createdDNA))
    return population

def executeBehavior(population):
    for i in range(len(population)):
        population[i].goto(population[i].xcor()+population[i].behavior[0]+population[i].giveShake()*population[i].shakeFactor
                           ,population[i].ycor()+population[i].behavior[1]+population[i].giveShake()*population[i].shakeFactor)
        population[i].weight = math.sqrt((population[i].xcor()-population[i].start_x)**2 + (population[i].ycor()-population[i].start_y)**2)
        #print(population[i].weight)

def getDNAWeights(pop):
    DNAs = []
    weights = []
    for i in range(len(pop)):
        DNAs.append(pop[i].dna)
        weights.append(pop[i].weight)
    weight_sum = sum(weights)
    probs = []
    for i in range(len(weights)):
        probs.append(weights[i]/weight_sum)
    dna_weights = [DNAs,probs,weights]
    return dna_weights




#print(population)
def breepPop(count,oldPop):
    population = []
    dna_weights = getDNAWeights(oldPop)
    for i in range(count):
        draw = numpy.random.choice(dna_weights[0], 2, p=dna_weights[1])
        bredDNA = breedDNA(draw[0],draw[1])
        population.append(createMember(start_area, bredDNA))
    return population



#########
#population = createPop(10)

#for i in range(10):
  #  executeBehavior(population)
 #   wn.clear()

#population2 = breepPop(10,population)

lMean=[]
lMax=[]

def logMeanMax(dna_weights):
    a1=round(numpy.mean(dna_weights[2]),0)
    a2=round(numpy.max(dna_weights[2]),0)
    lMean.append(a1)
    lMax.append(a2)
    return(a1,a2)


popSize = 10
cycles = 10
generations = 50


print("round","mean","max")
for i in range(generations):
    wn.clear()
    if i==0:
        population = createPop(popSize)
    else:
        population = breepPop(10, population)
    for j in range(cycles):
        executeBehavior(population)
    c = logMeanMax(getDNAWeights(population))
    print(i,c)


print(lMean)
print(lMax)



wn.bye()
#wn.exitonclick()


import pylab
#pylab.__version__


pylab.plot(list(range(generations)),lMean)
pylab.show()

pylab.plot(list(range(generations)),lMax)
pylab.show()