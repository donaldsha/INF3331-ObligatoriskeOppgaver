# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:08:19 2017

@author: donalds
"""
import math as mt
import numpy as np
from integrator import midpoint_integrate_constant
from numba_integrator import midpoint_integrate_numba
from numpy_integrator import midpoint_integrate_numpy


def test_midpoint_constant_function():
    expected_answer1 = 2
    computed_answer1 = midpoint_integrate_constant(lambda x:mt.sin(x), 0, mt.pi, 1000)
    #print(computed_answer1)
    #tester nå om forventet resulat er samme som resultatet vi fikk
    if(abs(computed_answer1 - expected_answer1) < 1E-5):#har minsket den siden det blir for stor
        print("Test midpoint_constant Passed for f(x)=sin(x), 0<x<pi, N=1000")
    else:
        print("Test midpoint_constant Failed for f(x)=sin(x), 0<x<pi, N=1000")


def test_midpoint_numpy_function():
    expected_answer1 = 2
    computed_answer1 = midpoint_integrate_numpy(lambda x:np.sin(x), 0, np.pi, 1000)
    #print(computed_answer1)
    #tester nå om forventet resulat er samme som resultatet vi fikk
    if(abs(computed_answer1 - expected_answer1) < 1E-5):
        print("Test midpoint_numpy Passed for f(x)=sin(x), 0<x<pi, N=1000")
    else:
        print("Test midpoint_numpy Failed for f(x)=sin(x), 0<x<pi, N=1000")


def test_midpoint_numba_function():
    expected_answer1 = 2
    computed_answer1 = midpoint_integrate_numba(lambda x:mt.sin(x), 0, mt.pi, 1000)
    #print(computed_answer1)
    #tester nå om forventet resulat er samme som resultatet vi fikk
    if(abs(computed_answer1 - expected_answer1) < 1E-5):
        print("Test midpoint_numba passed for f(x)=sin(x), 0<x<pi, N=1000")
    else:
        print("Test midpoint_numba Failed for f(x)=sin(x), 0<x<pi, N=1000")


#Kjøringer
test_midpoint_constant_function()
test_midpoint_numpy_function()
test_midpoint_numba_function()