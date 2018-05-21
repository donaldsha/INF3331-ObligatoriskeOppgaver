# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:05:27 2017

@author: donalds
"""
from integrator import integrate
from numpy_integrator import numpy_integrate
from numba_integrator import numba_integrate
import timeit #to check runtime


def test_integral_of_constant_function():
    expected_answer1 = 2
    computed_answer1 = integrate(lambda x:2, 0, 1, 100)

    #tester nå om forventet resulat er samme som resultatet vi fikk
    if(abs(computed_answer1 - expected_answer1) < 1E-20):
        print("Test passed for f(x)=2")
    else:
        print("Test Failed for f(x)=2")



def test_integral_of_linear_function():
    start_time = timeit.default_timer() #for tidssjekk

    expected_answer1 = 7500
    computed_answer1 = integrate(lambda x:x*6, 0, 50, 100000)
    #print(computed_answer1)

	#tester nå om forventet resulat er samme som resultatet vi fikk
    if(abs(computed_answer1 - expected_answer1) < 1E-20):
        print("Test passed for f(x)=6x")
        print("total time: ", (timeit.default_timer()-start_time))
    else:
        print("Test Failed for f(x)=6x")
        print("total time: ", (timeit.default_timer()-start_time))


def test_integral_with_numpy():
    start_time2 = timeit.default_timer() #for tidssjekk

    expected_answer1 = 7500
    computed_answer1 = numpy_integrate(lambda x:x*6, 0,50, 100000)
    #print(computed_answer1)

	#tester nå om forventet resulat er samme som resultatet vi fikk

    if(abs(computed_answer1 - expected_answer1) < 1E-20):
        print("Test passed for f(x)=6x")
        print("total time: ", (timeit.default_timer()-start_time2))

    else:
        print("Test Failed for f(x)=6x")
        print("total time: ", (timeit.default_timer()-start_time2))

    print("\nResult from the second NUMPY test: . . . \n")

    #start_time3 = datetime.now() #for tidssjekk

    expected_answer2 = 2500
    computed_answer2 = numpy_integrate(lambda x:2*x, 0, 50, 10000)

    if(abs(computed_answer2 - expected_answer2) < 1E-20):
        print("Test passed for f(x)=2x")
        #print("total time: ", (datetime.now()-start_time3))
    else:
        print("Test Failed for f(x)=2x")
        #print("total time: ", (datetime.now()-start_time3))


def test_integral_with_numba():
    #start_time4 = timeit.default_timer() #for tidssjekk

    expected_answer1 = 7500
    computed_answer1 = numba_integrate(lambda x:x*6, 0, 50, 1000)
    #print(computed_answer1)

	#tester nå om forventet resulat er samme som resultatet vi fikk
    if(abs(computed_answer1 - expected_answer1) < 1E-20):
        print("Test passed for f(x)=6x")
        #print("total time: ", (timeit.default_timer()-start_time4))
    else:
        print("Test Failed for f(x)=6x")
        #print("total time: ", (timeit.default_timer()-start_time4))

    print("Result from the second NUMBA test: . . . \n")

    #start_time5 = datetime.now() #for tidssjekk

    expected_answer2 = 2500
    computed_answer2 = numba_integrate(lambda x:2*x, 0, 50, 1000)
    #print(computed_answer2)

    if(abs(computed_answer2 - expected_answer2) < 1E-20):
        print("Test passed for f(x)=2x")
        #print("total time: ", (datetime.now()-start_time5))
    else:
        print("Test Failed for f(x)=2x")
        #print("total time: ", (datetime.now()-start_time5))

    #print("total time: ", (datetime.now()-start_time2))

#Skriver ut alle overste testene

print("\n **********Results from the CONSTANT function********* \n")
test_integral_of_constant_function()#run the tests for integrator
print("\n **********Results from the Linear function********* \n")
test_integral_of_linear_function()
print("\n **********Results from the NUMPY function********* \n")
test_integral_with_numpy()#run tests for numpy_integrator
print("\n **********Results from the NUMBA function********* \n")
test_integral_with_numba()#test numba


print("\n **********TEST FINISHED********* \n")