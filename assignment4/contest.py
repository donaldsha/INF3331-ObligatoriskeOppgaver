# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 18:51:39 2017

@author: donalds
"""
import numpy as np
from numpy_integrator import numpy_integrate

#her kjører jeg alle funksjonene og ser hva resultatet blir

def test_integral_with_numpy_contest():

    computed_answer1 = numpy_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin((x/3))/(x/3))*(np.sin((x/5))/(x/5))), 0, 50, 10000)
    print("første: ", computed_answer1)


    computed_answer2 = numpy_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin((x/3))/(x/3))*(np.sin((x/5))/(x/5))*(np.sin((x/7))/(x/7))), 0, 50, 10000)
    print("andre: ", computed_answer2)

    computed_answer3 = numpy_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin((x/3))/(x/3))*(np.sin((x/5))/(x/5))*(np.sin((x/7))/(x/7))*(np.sin((x/9))/(x/9))*(np.sin((x/11))/(x/11))), 0, 50, 10000)
    print("tredje: ", computed_answer3)

    computed_answer4 = numpy_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin((x/3))/(x/3))*(np.sin((x/5))/(x/5))*(np.sin((x/7))/(x/7))*(np.sin((x/9))/(x/9))*(np.sin((x/11))/(x/11))*(np.sin((x/13))/(x/13))), 0, 50, 10000)
    print("fjerde: ", computed_answer4)

    computed_answer5 = numpy_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin((x/3))/(x/3))*(np.sin((x/5))/(x/5))*(np.sin((x/7))/(x/7))*(np.sin((x/9))/(x/9))*(np.sin((x/11))/(x/11))*(np.sin((x/13))/(x/13))*(np.sin((x/15))/(x/15))), 0, 50, 10000)
    print("femte: ", computed_answer5)

    computed_answer6 = numpy_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin((x/4))/(x/4))*(np.sin((x/4))/(x/4))*(np.sin((x/7))/(x/7))*(np.sin((x/7))/(x/7))*(np.sin((x/9))/(x/9))*(np.sin((x/9))/(x/9))), 0, 50, 10000)
    print("sjette: ", computed_answer6)


test_integral_with_numpy_contest()