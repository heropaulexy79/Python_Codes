"""
Author: heropaulexy
Date: 23rd September 2018
Program to implement the crammer's rule
"""

'''
The equation is given in this order
a+b+c=d
e+f+g=h
i+j+k=l
'''
def main():
    try:
        a=float(input("Please enter value for a:\n"))
        b=float(input("Please enter value for b:\n"))
        c=float(input("Please enter value for c:\n"))
        d=float(input("Please enter value for d:\n"))
        e=float(input("Please enter value for e:\n"))
        f=float(input("Please enter value for f:\n"))
        g=float(input("Please enter value for g:\n"))
        h=float(input("Please enter value for h:\n"))
        i=float(input("Please enter value for i:\n"))
        j=float(input("Please enter value for j:\n"))
        k=float(input("Please enter value for k:\n"))
        l=float(input("Please enter value for l:\n"))

        initial=a*(f*k-j*g)-b*(e*k-g*i)+c*(e*j-i*f)
        first=d*(f*k-j*g)-b*(h*k-g*l)+c*(h*j-f*l)
        second=a*(h*k-g*l)-d*(e*k-i*g)+c*(e*l-h*i)
        third=a*(f*l-h*j)-b*(e*l-h*i)+d*(e*j-i*f)

        x1=first/initial
        x2=second/initial
        x3=third/initial

        print("The roots are X1=",x1,"\n X2=",x2,"\n X3=",x3)
    except Exception as e:
        print("Only digits are allowed!!!")
        main()

main()