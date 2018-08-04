'''REGULAR POLYGON'''
import math
s=float(input('Enter the length of side:'))
n=int(input('Enter the number of sides:'))
a=(s*s*n)/(4*(math.tan((math.pi)/n)))
print('Area of regular polygon=%f'%(a))
