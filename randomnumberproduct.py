'''A program that generates a random number, x, between 1 and 50, 
a random number y between 2 and 5, and computes x*y.''' 
import random
x=random.randrange(1,50)
print('Random number 1=',x)
y=random.randrange(2,5)
print('Random number 2=',y)
print('The product of random numbers =',x*y)