'''NAMING A TRIANGLE'''
a,b,c=map(int,input('Enter the 3 lengths of a triangle:').split(' '))
if a==b==c:
	print('Triangle is equilateral')
elif a==b or a==c or b==c:
	print('Triangle is isosceles')
else:
	print('Triangle is scalene')