'''Dan is playing a video game in which his character competes in a hurdle race. 
Hurdles are of varying heights, and Dan has a maximum height he can jump. 
There is a magic potion he can take that will increase his maximum height by unit for each dose. 
How many doses of the potion must he take to be able to jump all of the hurdles.
Given an array of hurdle heights "height", and an initial maximum height Dan can jump, "k" 
determine the minimum number of doses Dan must take to be able to clear all the hurdles in the race.
example: 
input
k= 4
height=1 6 3 5 2
output 
 2'''
height=[]
dmax=int(input('Enter the maximum height dan can jump:'))
print('Enter the hurdle heights:')
l=input()
while l!='':
	height.append(int(l))
	l=input()
s=max(height)
if dmax>=s:
	print('No need for dan to take magic portion!!!')
else:
	print('Minimum number of doses dan must take=',s-dmax)
	
'''TESTCASES
----------------------------------------------------
Enter the maximum height dan can jump:4
Enter the hurdle heights:
3
4
2
1

No need for dan to take magic portion!!!
-----------------------------------------------------
Enter the maximum height dan can jump:6
Enter the hurdle heights:
1
3
2
4

No need for dan to take magic portion!!!
--------------------------------------------------------
Enter the maximum height dan can jump:5
Enter the hurdle heights:
4
8
10
12
5
7

Minimum number of doses dan must take= 7
'''
