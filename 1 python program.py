1.withot input functions
=====================
a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)


2.with input functions
=====================
a=eval(input("enter first number:"))
b=eval(input("enter second number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)



3.accept two values and perform swapping of two numbers
=====================================================
a=int(input("enter first number:"))
b=int(input("enter second number:"))
temp=a
a=b
b=temp
print("after swapping of two numbers are:")
print("---------------------------------")
print("first value is:",a)
print("second value is:",b)


4.area of triangle
================
a=int(input("enter first side of the triangle:"))
b=int(input("enter second side of the triangle:"))
c=int(input("enter third side of the triangle:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of the triangle is",area)


5.area and perimeter of rectangle
================================
l=eval(input("enter the length of the rectangle:"))
b=eval(input("enter the breadth of the rectangle:"))
area=l+b
perimeter=2*(l+b)
print("area of rectangle is:",perimeter)


6.circumference of the circle
===========================
pi=3.14
d=eval(input("enter the diameter of the circle:"))
r=d/2
circumference=2*pi*r
print("circumference of the circle for the given diameter is",circumference)



6.1 radius of the circle
====================
diameter=eval(input("enter the diameter:"))
radius=diameter/2
print("radius of circle is:",radius)



7.comparision operators
=====================
a=10
b=20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
