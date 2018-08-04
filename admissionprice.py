'''A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge. 
Children between 3 and 12 years of age cost $14.00. 
Seniors aged 65 years and over, cost $18.00.
Admission for all other guests is $23.00.
Create a program that begins by reading the ages of all of the guests in a group from the user,
with one age entered on each line. 
The user will enter a blank line to indicate that there are no more guests in the group. 
Then your program should display the admission cost for the group with an appropriate message. 
The cost should be displayed using two decimal places.'''
age=[]
cost=0
print('Enter the ages of members:')
l=(input())
while l!='': 
	age.append(int(l))
	l=input()
for i in age:
	if i<=2:
		cost=cost+0
	elif i>=3 and i<=12:
		cost=cost+14
	elif i>=65:
		cost=cost+18
	else:
		cost=cost+23
if cost==0:
	print('Enter a valid input!!!')
else:
	print('Total cost of admission = $ %.2f'%(cost))
		