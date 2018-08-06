'''A program that asks the user to enter a word and 
prints out whether that word contains any vowels.'''
str=input('Enter a word:')
vow=['a','e','i','o','u','A','E','I','O','U']
l=[]
flag=0
for i in str:
	if i in vow:
		l.append(i)
		flag=1
if flag!=1:
	print('The word doesn\'t contain any vowels!!!')
else:
	print('The word contains vowels and they are,')
	for i in l:
		print(i)
