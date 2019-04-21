#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 01:27:32 2018

@author: jl
"""
import numpy as np
import copy


def Robby(path,u):

    l = len(u)
    maxpoint=500
    E=0      
    pi=[0,0]

    def evaluate(p,e,l):
        if p[0]<0:
            e=e-5
            p[0]=0
            
        if p[1]<0:
            e=e-5
            p[1]=0
        if p[0]>l-1:
            e=e-5
            p[0]=l-1
        if p[1]>l-1:
            e=e-5
            p[1]=l-1
        return [p,e]

    world = copy.deepcopy(u)

        
    for j in path:
        if j==0:
            pi[0]=pi[0]+1
            [pi,E]=evaluate(pi,E,l)

        elif j==1:
            pi[0]=pi[0]-1 
            [pi,E]=evaluate(pi,E,l)

        elif j==2:
            pi[1]=pi[1]+1
            [pi,E]=evaluate(pi,E,l)

        elif j==3:
            pi[1]=pi[1]-1
            [pi,E]=evaluate(pi,E,l)

        elif j==4:
            pi=pi
        else:
            if world[pi[0]][pi[1]]==1:
               world[pi[0]][pi[1]]=0
               E=E+50
            else:
                E=E-1       

    return E


def Board(siz, num_obstacles=10):
    """
    This function creates a bord where the simulation of Robby takes place
    :param siz: size of the board
    :param num_obst: nummber of obstacles
    :return:
    """
    # Generate s an array W of size siz x siz
    w = np.zeros((siz, siz))
    r = []

    for i in range(num_obstacles):
        # generate two random numbers corresponding to the coordinates of the obstacles the board
        r_x = np.random.randint(siz-1)
        r_y = np.random.randint(siz-1)
        w[r_x, r_y] = 1
        r.append([r_x, r_y])

    return [w, r]


def pop_generator(size_pop=100, num_instruct=200):

    """

    :param size_pop: number of individuals in the initial population (default = 100)
    :param num_instruct: number of instructions that each individual will have (default = 200)
    :return: A lit with each of the different individuals
    """
    
    p = []
    for i in range(size_pop):
        p.append(np.random.randint(6, size=num_instruct))
        
    return p
