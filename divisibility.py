'''input a number k and an array 
There is an array  find all possible pairs of numbers which when added is divisible by the number k 
output count of successfully divisible pairs'''
arr=[]
divisible=[]
count=0
print('Enter the array elements:')
l=input()
while l!='':
	arr.append(int(l))
	l=input()
k=int(input('Enter a number:'))	
i=0
l=len(arr)
while i!=l:
	j=i+1
	while j!=l:
		num=arr[i]+arr[j]
		if num%k==0:
			divisible.append(num)
			count=count=count+1
		j=j+1
	i=i+1
		
print('Number of elements divisible by :',count)
'''TESTCASES
------------------------------------------------------------
Enter the array elements:
3
5
7
2

Enter a number:4
Number of elements divisible are: 2
---------------------------------------------------------------
Enter the array elements:
2
3
4
2

Enter a number:5
Number of elements divisible are: 2
'''

	
   