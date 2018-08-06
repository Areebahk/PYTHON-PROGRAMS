'''Write a program that asks the user for a large integer 
and inserts commas into it according to the standard American convention. 
For instance, if the user enters 1000000, the output should be 1,000,000.'''
num=input('Enter a number:')
#number reversed
reversed=num[::-1]
count=0
l=[]
for i in reversed:
	#inserting comma after every third number
	if (count%3)==0 and count!=0:
		l.append(',')
	#appending each digit to a list,l
	l.append(i)
	count=count+1
#joining elements of list to get the number
numbr=''.join(l)
#reversing the number 
numbr=numbr[::-1]
print('According to american convention',num,'is represented as :',numbr)
