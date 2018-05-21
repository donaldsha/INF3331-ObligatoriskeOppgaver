# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:05:27 2017

@author: donalds
"""
import math as mat
import numpy as np

def numpy_integrate(f, a, b, N):
    i = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fi = f(i)
    arealet = np.sum(fi)*(b-a)/N
    return arealet


def midpoint_integrate_numpy(f, a, b, N):
    res = ((b - a)/N)
    s = np.linspace((a + res/2), (b - res/2), N)
    return np.sum(f(s))*res

#print(midpoint_integrate_numpy(lambda x:np.sin(x), 0, np.pi, 100))