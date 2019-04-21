#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 01:27:32 2018

@author: jl
"""
import numpy as np
import copy
from matplotlib import pyplot as plt


def Robby(path, u):

    """
    This is the function which evaluates how good each individual performs and it follow the next rules:
    * The initial point is always at the cell (0,0).
    * Robby can move up, down right or left inside the board
    * If it moves out of the boundaries it is penalized with -1 point
    * It can also pick bottles in the ground
    * If it decides to pick up in a cell where there is nothing it gets penalized with -5 points
    * If it picks up in a cell where there is a bottle it is rewarded with +50 points

    :param path: the list of instructions of each individual
    :param u:
    :return: the score of the evaluation
    """

    l = len(u)
    evaluation = 0
    initial_point = [0, 0]

    def evaluate(point, evaluation, l):
        if point[0] < 0:
            evaluation = evaluation-5
            point[0] = 0
            
        if point[1] < 0:
            evaluation = evaluation-5
            point[1] = 0

        if point[0] > l-1:
            evaluation = evaluation-5
            point[0] = l-1

        if point[1] > l-1:
            evaluation = evaluation-5
            point[1] = l-1

        return [point, evaluation]

    world = copy.deepcopy(u)

    for j in path:
        # moves one step to x+
        if j == 0:
            initial_point[0] = initial_point[0]+1
            [initial_point, evaluation] = evaluate(initial_point, evaluation, l)

        # moves one step to x-
        elif j == 1:
            initial_point[0] = initial_point[0]-1
            [initial_point, evaluation] = evaluate(initial_point, evaluation, l)

        # moves one step to y+
        elif j == 2:
            initial_point[1] = initial_point[1]+1
            [initial_point, evaluation] = evaluate(initial_point, evaluation, l)

        # moves one step to y-
        elif j == 3:
            initial_point[1] = initial_point[1]-1
            [initial_point, evaluation] = evaluate(initial_point, evaluation, l)

        # stays still
        elif j == 4:
            initial_point = initial_point

        # checks if there is a can in that position
        else:
            # if it is true, picks the can and earns 50 points
            if world[initial_point[0]][initial_point[1]] == 1:
               world[initial_point[0]][initial_point[1]] = 0
               evaluation = evaluation+50

            # else it looses one point
            else:
                evaluation = evaluation-1

    return evaluation


def gen_algot(init_pop, fx, fit_func, generations, mutation_r):

    """

    :param init_pop: list with the initial population
    :param fx: function to solve, in this case the problem of the Board with obstacles
    :param fit_func: Fit function, i.e. the function that will determine which individual of the population is better
    fit than the others
    :param generations: number of times that the program will be iterated
    :param mutation_r: mutation rate, a probability between [0,1] that an instruction in any individual will change randomly
    :return: a list of  1. the final population of individuals.
                        2. a time history of the best performances.
                        3. a time history of the average performances
                        4. the best performance of all
                        5. an list with the best individuals of each generation

    """

    new_population = []
    best_performance = []
    worst_performance = []
    average_performance = []
    best_indivdual = []
    global ni
    ni = []

    # ======================evaluation of the fitness =======================
    ti = 0
    while ti < generations:

        evaluation = []
        for individual in init_pop:
            ev = fit_func(individual, fx)
            evaluation.append(np.asarray(ev))

        # saves the best performance and the average
        best_performance.append(min(evaluation))
        worst_performance.append(max(evaluation))
        average_performance.append(np.mean(evaluation))
        best_indivdual.append(init_pop[evaluation.index(max(evaluation))])

        # ================= reproduction =====================================
        n = 0
        while n < len(init_pop):
            # normalize the result, first get rid off the negatives
            if min(evaluation) < 0:
                evaluation = [i + (-min(evaluation)) for i in evaluation]

            # then divide each one by the one with maximum value
            norm = max(evaluation)
            evaluation = [(x * 1.0000 / norm) for x in evaluation]

            # ++++++++++++++++  Here begins the actual Genetic Algorithm ++++++++++++++++++++
            # ===============================================================================

            # choose 2 random individuals
            i1 = np.random.randint(len(init_pop))
            i2 = np.random.randint(len(init_pop))

            # if their performance is higher than a random number r

            if evaluation[i1] > np.random.random() and evaluation[i2] > np.random.random():

                # --------- then create a new individual------------------
                ni = []

                for j in range(len(init_pop[i1])):
                    if np.random.randint(2) == 1:
                        ni.append(init_pop[i1][j])
                    else:
                        ni.append(init_pop[i2][j])

                # ------------------ad mutation-------------------------
                # generate a random number, if the random number is smaller than the mutation rate
                if np.random.random() < mutation_r and ni != []:
                    rr1 = np.random.randint(len(ni))
                    rr2 = np.random.randint(len(ni))
                    if rr1 >= rr2:
                        ni[rr1] = ni[rr2]

                new_population.append(np.asarray(ni))
                n = n + 1

        init_pop = copy.deepcopy(new_population)
        new_population = []
        ti = ti + 1
        print(ti)

    return [init_pop, best_performance, average_performance, worst_performance, best_indivdual]


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


def visualzation(string, obstacles, l):

    def validate(point, l):

        if point[0] < 0:
            point[0] = 0

        if point[1] < 0:
            point[1] = 0

        if point[0] > l - 1:
            point[0] = l - 1

        if point[1] > l - 1:
            point[1] = l - 1

        return point

    print(string)
    print(obstacles)

    plt.figure()

    initial_point = [0, 0]

    for instruction in string:
        plt.plot(initial_point[0],initial_point[1], 'ob')
        print(instruction)
        points_x = [point[0] for point in obstacles]
        points_y = [point[1] for point in obstacles]

        # moves one step to x+
        if instruction == 0:
            initial_point[0] = initial_point[0] + 1
            initial_point = validate(initial_point, l)

        # moves one step to x-
        elif instruction == 1:
            initial_point[0] = initial_point[0] - 1
            initial_point= validate(initial_point, l)

        # moves one step to y+
        elif instruction == 2:
            initial_point[1] = initial_point[1] + 1
            initial_point = validate(initial_point, l)

        # moves one step to y-
        elif instruction == 3:
            initial_point[1] = initial_point[1] - 1
            initial_point = validate(initial_point, l)

        # stays still
        elif instruction == 4:
            initial_point = initial_point

        # checks if there is a can in that position
        else:
            # if it is true, picks the can and earns 50 points
            if initial_point in obstacles:
                obstacles.remove(initial_point)

        plt.plot(points_x, points_y, '*r')
        plt.pause(0.01)
        plt.clf()

    plt.axis([0, l, 0, l])
    plt.show()


