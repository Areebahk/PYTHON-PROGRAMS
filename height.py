'''HEIGHT UNITS'''
f,i=map(int,input('Enter the height of a man in feets and inches: ').split('.'))
cm=((f*12)+i)*2.54
print('Height of man in cm=%f'%(cm))
