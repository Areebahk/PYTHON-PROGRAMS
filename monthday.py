''' MONTH AND THE CORRESPONDING DAYS'''
month31=['january','march','may','july','august','october','december']
month30=['april','june','september','november']
m=input('Enter a month:')
if m in month31:
	print(m,'has 31 days')
elif m in month30:
	print(m,'has 30 days')
else:
	print(m,'can have 28 or 29 days')