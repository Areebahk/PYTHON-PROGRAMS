'''UNITS OF TIME'''
d,h,m,s=map(int,input('Enter the number of days,hours,minute and second (: separation)= ').split(':'))
tot_sec=(d*24*60*60)+(h*60*60)+(m*60)+s
print('Total number of seconds=%d'%(tot_sec))
sec=int(input('Enter the total number of seconds='))
day=sec/(60*60*24)
sec=sec%(60*60*24)
hr=int(sec/(60*60))
if hr<10:
	hr='0'+str(hr)
else:
	hr=str(hr)
sec=sec%(60*60)
min=int(sec/60)
if min<10:
	min='0'+str(min)
else:
	min=str(min)
sec=sec%60
if sec<10:
	sec='0'+str(sec)
else:
	sec=str(sec)
print('Duration = %2d:%2s:%2s:%2s'%(day,hr,min,sec))