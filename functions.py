import turtle
import random
import math
import operator
import time

import numpy


def createMember(start_area,DNA,canvaswidth,canvasheight):
    member = turtle.Turtle()




    member.dna = DNA
    member.behavior = [member.dna.xMove,member.dna.yMove]
    member.shakeFactor = member.dna.shake

    member.start_x = member.dna.xstart
    member.start_y = member.dna.ystart

    member.giveShake = giveShake
    member.weight=0
    member.obsTrip = 0


    member.speed(0)
    member.penup()
    member.goto(member.start_x,member.start_y)

    return member



def giveShake():
    return random.randint(-10,10)




class DNA:
    def __init__(self):
        range = 0
        self.shake = random.uniform(0,3)
        self.xMove = random.randint(0, 60)
        self.yMove = random.randint(-10, 10)

        self.xstart = random.randint(0, 300)
        self.ystart = random.randint(0+range, 1000-range)




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
        newDNA.xstart = dna1.xstart
    else:
        newDNA.xstart = dna2.xstart

    if random.randint(0,1) ==0:
        newDNA.ystart = dna1.ystart
    else:
        newDNA.ystart = dna2.ystart



    return newDNA



def createPop(count,start_area,canvaswidth,canvasheight):
    population = []
    for i in range(count):
        createdDNA = DNA()
        population.append(createMember(start_area,createdDNA,canvaswidth,canvasheight))
    return population


def breepPop(count,oldPop,start_area,canvaswidth,canvasheight):
    population = []
    dna_weights = getDNAWeights(oldPop)
    for i in range(count):
        draw = numpy.random.choice(dna_weights[0], 2, p=dna_weights[1])
        bredDNA = breedDNA(draw[0],draw[1])
        population.append(createMember(start_area, bredDNA,canvaswidth,canvasheight))
    return population



def getDNAWeights(pop):
    DNAs = []
    weights = []
    for i in range(len(pop)):
        DNAs.append(pop[i].dna)
        if pop[i].obsTrip == 1:
            weights.append(0)
        else:
            weights.append(pop[i].weight)
    weight_sum = sum(weights)
    probs = []
    for i in range(len(weights)):
        probs.append(weights[i]/weight_sum)
    dna_weights = [DNAs,probs,weights]
    return dna_weights


def logMeanMax(dna_weights):
    a1=round(numpy.mean(dna_weights[2]),0)
    a2=round(numpy.max(dna_weights[2]),0)
    lMean.append(a1)
    lMax.append(a2)
    return(a1,a2)
