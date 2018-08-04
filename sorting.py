''' SORTING 3 INTEGERS'''
a,b,c=map(int,input('Enter 3 numbers(separated by space):').split(' '))
print('''After sorting integers are''',min(a,b,c),(a+b+c-min(a,b,c)-max(a,b,c)),max(a,b,c))