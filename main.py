"""
Solution for the Decode Demcon Challenge: Even Fibonacci numbers

This solution makes use of a formula to calculate even fibonacci numbers 
based on the current and previous even fibonacci number. 
Calculations are performed in matrix form, 
where the sum of the even fibonacci numbers is included in the equation.   

Author: @Jeroenvs513
"""

import numpy as np          # import numpy library for matrix multiplications

'''Input'''
t=4e6                       # treshold to which even fib. numbers must be summed (must be >2)

'''Init'''
# State vector:
x = np.array([[2],          # even fib. number,
              [0],          # previous even fib. number,
              [2]])         # sum of even fib. numbers up to and including x[0]
# State transition matrix:
A = np.array([[4, 1,0],     # calc. of next even fib. number (= 4* current + 1* previous even fib. number),
              [1, 0,0],     # previous fib. number is replaced with current,
              [4, 1,1]])    # calc. of the sum of even fib. numbers

'''Calculation'''
while (4*x[0] + x[1] < t):  # loop until treshold is about to be exceeded
    x=np.dot(A,x)           # calculate new state vector: x[n+1]=A*x[n]

'''Output'''
print('\n The largest even fibonacci number below the treshold of %d is: %d,' 
      '\n the sum of al even fibonacci numbers up to and including this value is: %d.' % (t,x[0,0],x[2,0]))