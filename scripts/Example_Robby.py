#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 23:28:41 2018

@author: jl
"""

from genetic_algorythms import gen_algot
from Roby_gen import* 
import matplotlib.pyplot as plt


"""
This is an implementation of the example "Robby" found in the book:

Complexity a guided tour by Melanie Mitchell. 
The script is an implementation of fa Genetic Algorithm to solve the problem as proposed in the book (p 131)
"""

# number of different 'individuals' in the initial population of instructions
population = 100
#  number of instructions that each individual will have
num_instruct = 200
# number of generations to iterate
generations = 1000
# size of the board
siz = 10
# Generates a Board, with X number of obstacles, by default 10
[w, p] = Board(siz, 10)
# generates a population of N individuals with S number of instructions each one
pop_i = pop_generator(population, num_instruct)
# implements the genetic algorithm
[pp, pe, pa, be, br] = gen_algot(pop_i, w, Robby, generations, 0.3)

# #########========================FIGURES========================
plt.figure(1)
plt.plot(p, 'go')
plt.xlabel(['X axis'])
plt.ylabel(['Y axis'])
plt.ylim(0, siz-1)
plt.xlim(0, siz-1)
plt.show()


plt.figure(2)
plt.plot(pe, '-*g')
plt.plot(pa, '-+r')
plt.xlabel(['X'])
plt.ylabel(['Fitnes'])
plt.show()

#pe[:]=[i+(-min(pe)) for i in pe]
#pe = [x*1.0 / max(pe) for x in pe]
#
#plt.figure(3)
#plt.plot(eve,'-o')
#plt.xlabel(['X'])
#plt.ylabel(['Fitnes'])
#plt.show()

#pi=[0,0]
#plt.figure(4)
#l=len(w)
#for j in pp[50]: 
#    
#    plt.clf()
#    if j==0:
#        pi[0]=pi[0]+1
#    elif j==1:
#        pi[0]=pi[0]-1 
#    elif j==2:
#        pi[1]=pi[1]+1
#    elif j==3:
#        pi[1]=pi[1]-1
#    elif j==4:
#        pi=pi
#    elif j==5:
#        if (pi in p)==True:
#            p.pop(p.index(pi))
#  
#    if pi[0]<0:
#        pi[0]=0
#        
#    if pi[1]<0:
#        pi[1]=0
#        
#    if pi[0]>l-1:
#        pi[0]=l-1
#        
#    if pi[1]>l-1:
#        pi[1]=l-1
#        
#    print(pi)       
#    plt.plot(pi,'*')
#    plt.plot(p,'go')
#    plt.pause(0.001)
#
#plt.show()

    