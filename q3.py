''' ACCEPT FROM THE USER: DAYS IN FUTURE
	DISPLAY: FUTURE DAY+SUPERSCRIPT(st,nd,rd,th), MONTHNAME, YEAR'''
	
monthdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
st=[1,21,31]
nd=[2,22]
rd=[3,23]
month={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

#Accepting date

d,m,y=map(int,input('Enter the date:').split('-'))
f=int(input('Enter the future number of days:'))

#Validation

if ((y%400==0) or (y%4==0 and y%100!=0)) and m==2:
	monthdays[2]=29
if y<1000 or y>3000:
	print('Enter valid year!!!')
if m > 12 or m<1:
	print('Wrong date!!!')
	exit()
if d<1 or d>monthdays[m]:
	print ('Wrong date!!!')
	exit()

#Finding the future date

while f!=0:
	if m==12 and d==31:			#Next year
		y=y+1
		d=1
		m=1
	elif monthdays[m]==d:		#Next month
		d=1
		m=m+1
	else:						#Normal day
		d=d+1
	f=f-1

#Finding the date with superscript

if d in st:
	print('Date : %dst %s,%d'%(d,month[m],y))
elif d in nd:
	print('Date : %dnd %s,%d'%(d,month[m],y))
elif d in rd:
	print('Date : %drd %s,%d'%(d,month[m],y))
else:
	print('Date : %dth %s,%d'%(d,month[m],y))
