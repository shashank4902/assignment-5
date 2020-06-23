#find area of regular polygon
gravity=9.8
length=float(input("enter the length of each side of polygon(in meters:"))
number=int(input("enter the number of sides:"))
area=(number*length**2)/(4*tan(pi/number))
print("the area of polygon is %2f"%area)