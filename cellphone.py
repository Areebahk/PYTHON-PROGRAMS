'''CELL PHONE BILL'''
mint=int(input('Enter total minute:'))
msg=int(input('Enter total message sent:'))
print('Base charge = $15')
amint=0
amsg=0
if mint>50:
	amint=(mint-50)*.25
	print('Additional minute charge = $%.2f'%(amint))
if msg>50:
	amsg=(msg-50)*.15
	print('Additional message charge = $%.2f'%(amsg))
print('911 charge = $0.44')
total=15+amint+amsg+.44
print('Total charge = $%.2f'%(total))
tax=.05*total
print('Tax = $%.2f'%(tax))
print('Final amount to be payed = $%.2f'%(total+tax))



