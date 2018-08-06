'''A program that asks the user for a string 
and returns an estimate of how many words are in the string'''
str=input('Enter a string:')
l=str.split(' ')
#counting whether there is multiple spaces between 2 words
cnt=l.count('')
print('Number of words in string=',len(l)-cnt)
