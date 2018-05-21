# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:51:14 2017

@author: donalds
"""
import numba as num

def numba_integrate(f, a, b, N):
    func=num.jit(nopython=True)(f)
    @num.jit
    def function(a, b, N):

        res = (b - a)/N
        x=0.0;
        x += func(a)/2.0
        for i in range(1,N):
            x += func(a + i*res)
        x += f(b)/2.0
        return x*res #trapezoid regelen
    return function(a, b, N)


def midpoint_integrate_numba(f, a, b, N):
    res = float((b - a)/N)
    s = 0
    for x in range(N):
        s += f((a+res/2.0) + x*res)
    s *= res
    return s



"""
expected_answer1 = 1
computed_answer1 = numba_integrate(lambda x:2*x, 0, 1, 100)
print(computed_answer1)

	#tester nå om forventet resulat er samme som resultatet vi fikk
#start_time = timeit.timeit()
if(abs(computed_answer1 - expected_answer1) < 1E-20):
    print("Test passed for f(x)=2x")
else:
    print("Test Failed for f(x)=2x")


#print(numba_integrate(lambda x:2*x, 0, 1, 100))
"""