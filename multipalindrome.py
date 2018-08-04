'''MULTI WORD PALINDROME'''
w=input('Enter a string:')
word=w.replace(' ','')
l=len(word)
i=0
flag=0
while i!=l//2:
	if word[i]!=word[l-1-i]:
		flag=1
		break
	i=i+1
if flag==1:
	print('The string : %s is not palindrome' %(w))
else:
	print('The string : %s is palindrome' %(w))