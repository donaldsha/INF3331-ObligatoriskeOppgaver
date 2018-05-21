# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:05:27 2017

@author: donalds
"""
import math as mt
import matplotlib.pyplot as mtplot


def integrate(f, a, b, N):
    res = float(b - a)/N
    s = 0.0
    s+=f(a)/2.0
    for x in range(1, N):
        s+=f(a+x*res)
        #print(f(a+x*res))
    s+=f(b)/2.0 #trapezoid regelen
    return s*res


def midpoint_integrate_constant(f, a, b, N):
    res = ((b - a)/N)
    s = 0
    for x in range(N):
        s += f((a+res/2) + x*res)
    s *= res
    return s

#print(midpoint_integrate_constant(lambda x:mt.sin(x), 0, mt.pi, 1000))
#print(integrate(lambda x:x**2, 0, 2, 11))

def quadratic_error_plot(): #Basert på forelesning
    y = []
    x = []
    expected_answer = 1.0/3.0    #Resultatet vi letter etter
    for N in range(1, 50):
        x.append(N)
        computed_answer = integrate(lambda x:x**2, 0, 1, N)
        #print(computed_answer)
        y.append(abs(computed_answer - expected_answer))

    mtplot.plot(x, y, 'r', label="points") #for å få en linje bruker jeg r
    mtplot.ylabel('Errors')
    mtplot.xlabel('N')
    #mtplot.show()
    mtplot.draw()
    mtplot.savefig('quadratic_error.png', dpi=100)


quadratic_error_plot()





