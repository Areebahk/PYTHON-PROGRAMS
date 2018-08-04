''' TAX AND TIP '''
cost=float(input('Cost of meal	='))
tax_rate=.5
tip_rate=.1
tax=cost*tax_rate
tip=cost*tip_rate
total=cost+tax+tip
print('''
Cost of meal		= %f Rs
Tax         		= %f Rs
Tip         		= %f Rs
----------------------------------
Total       		= %f Rs
'''
%(cost,tax,tip,total))