'''REVERSING SECOND HALF OF A STRING'''
str=input('Enter a string: ')
length=len(str)
half=int(length/2)
part1=str[:half]
part2=str[half:]
part2=part2[::-1]
print('Required string is,%s%s'%(part1,part2))