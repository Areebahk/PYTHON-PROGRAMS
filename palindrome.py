'''STRING PALINDROME'''
word=input('Enter a string:')
l=len(word)
i=0
flag=0
while i!=l//2:
	if word[i]!=word[l-1-i]:
		flag=1
		break
	i=i+1
if flag==1:
	print(word,'is not palindrome')
else:
	print(word,'is palindrome')