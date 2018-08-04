'''Write a program that asks the user to enter a string. The program should then print the following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e
(k) The string with every letter replaced by a space'''
l=input('Enter a string:')
print('Total no: of characters = ',len(l))
print('String repeated 10 times:')
print(l*10)
print('First character:',l[0])
print('First 3 character:',l[0:3])
print('Last 3 character:',l[len(l)-4:len(l)])
print('String reversal:',l[::-1])
if len(l)>=7:
	print('Seventh character:',l[6])
else:
	print('Seventh character does not exist!!!')
print('String trimmed on both ends:',l[1:len(l)-1])
print('String capitalized:',l.upper())
print('All a replaced with e:',l.replace('a','e'))

