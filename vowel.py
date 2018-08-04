''' VOWEL OR CONSONANT'''
v=['a','e','i','o','u','A','E','I','O','U']
l=input('Enter an alphabet:')
for i in v:
	if i==l:
		print (l,"is a vowel")
		exit()
if l == 'y' or l== 'Y':
	print ('Sometimes Y is a consonant and sometimes a vowel')
else:
	print(l,'is a consonant')