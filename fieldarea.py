'''AREA OF FIELD'''
l=float(input('Length of field in feet ='))
w=float(input('Width of field in feet ='))
area=l*w
print('''
Length of field in feet 	  = %f feets
Width of field in feet  	  = %f feets
Area of field in square feets = %f 
Area of field in acres        = %f 
'''
%(l,w,area,area/43560))