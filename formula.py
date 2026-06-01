# write a program to find the roots of quadratic equation.
# x=-b±√b²-4ac/2a: Formula.
import math
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if a==0:
    l=-c/b
    print("the value of linear eqn is:",l)
    print("the value of a is zero so that it becomes linear equation not quadratic")
else:
    d=b*b-4*a*c
    print("discriminant of quadratic equation:",d)
    if d>0:
        z=(math.sqrt(d))
        print("sqrt of discriminant:",z)
        x1=(-b+z)/(2*a)
        print("first root of quadratic equation:",x1)
        x2=(-b-z)/(2*a)
        print("second root of quadratic equation:",x2)
    elif d<0:
      print("discriminant is negative so that sqrt can not be find:")



