'''An array a has to be rotated by the integer k places 
and the induces in the queries array has to be outputted.
It should return an array of integers representing the values at the specified indices.
a: an array of integers to rotate
k: an integer, the rotation count
queries: an array of integers, the indices to report'''
arr=[]
rot=[]
print('Enter the array elements:')
l=input()
while l!='':
	arr.append(int(l))
	l=input()
k=int(input('Enter rotation count:'))
print('Array elements are,')
print(arr)
l=len(arr)
neg=k*-1
while neg!=0:
	rot.append(arr[neg])
	neg=neg+1
i=0
while i<(l-k):
	rot.append(arr[i])
	i=i+1
print('Array after rotation is,')
print(rot)
'''TESTCASES
-------------------------------------------
Enter the array elements:
5
3
6
7
2
5
6

Enter rotation count:4
Array elements are,
[5, 3, 6, 7, 2, 5, 6]
Array after rotation is,
[7, 2, 5, 6, 5, 3, 6]
--------------------------------------------------
'''

	