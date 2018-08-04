'''NEXT DAY'''
monthdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
day,month,year=map(int,input('Enter the date:').split('-'))
if month==12 and day==31:
	year=year+1
	day=1
	month=1
elif ((year%400==0) or (year%4==0 and year%100!=0)) and month==2:
	if day==28:
		day=day+1
	elif day==29:
		day=1
		month=3
	else:
		day=day+1
elif monthdays[month]==day:
	day=1
	month=month+1
else:
	day=day+1
print('Next day is %d-%d-%d'%(day,month,year))


