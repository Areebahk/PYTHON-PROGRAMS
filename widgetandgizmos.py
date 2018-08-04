'''WIDGETS AND GIZMOS'''
w=int(input('Enter number of widgets = '))
g=int(input('Enter number of gizmos = '))
widget_weight=w*75
gizmos_weight=g*112
total_weight=widget_weight+gizmos_weight
print('''
Widgets	= %d
Gizmos	= %d
Widget weight	= %d
Gizmos weight	= %d
------------------------------------
Total weight	= %d
'''%(w,g,widget_weight,gizmos_weight,total_weight))