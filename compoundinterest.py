'''COMPOUND INTEREST '''
r=4
p=float(input('Enter the amount invested:'))
i1=float((p*r)/100)
a1=p+i1
i2=float((a1*r)/100)
a2=a1+i2
i3=float((a2*r)/100)
a3=a2+i3
print('Amount received after 1 year=%f'%(a1))
print('Amount received after 2 year=%f'%(a2))
print('Amount received after 3 year=%f'%(a3))


