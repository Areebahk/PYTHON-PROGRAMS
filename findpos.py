'''FINDING POSITION OF 0 '''
num=str(1203405607809)
c=num.count('0')
i=0
print('\n\n\nNumber of zeroes in %s= %d'%(num,c))
print('Zero is found in positions:')
while c>0:	
	c=c-1
	ind=num.find('0',i,len(num))
	print(ind+1)
	i=ind+1
