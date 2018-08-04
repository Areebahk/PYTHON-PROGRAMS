'''Julius Caesar protected his confidential information by encrypting it using a cipher. 
Caesar's cipher shifts each letter by a number of letters. 
If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.'''
alphabet='$abcdefghijklmnopqrstuvwxyzabcABCDEFGHIJKLMNOPQRSTUVWXYZABC'
str=input('Enter a string:')
str.replace(' ','$')	
l=list(str)
j=0
for i in l:
	c=alphabet.find(i)+3	
	if c==2:				
		l[j]='$'
	else:			
		l[j]=alphabet[c]	
	j=j+1
	str=''.join(l)			
	str=str.replace('$',' ')
print('Cipher is,%s'%(str))
'''TESTCASES
------------------------------------------------
Enter a string:hai
Cipher is,kdl
---------------------------------------
Enter a string:hai hello
Cipher is,kdl khoor
-------------------------------------------
Enter a string:SpArK
Cipher is,VsDuN
-------------------------------------------
Enter a string:good girl
Cipher is,jrrg jluo
'''