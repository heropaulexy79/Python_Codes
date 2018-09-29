"""
Author: Heropaulexy
Date:18th September 2018
Using lists in python
"""

"""
name=[]
number=int(input("How many names do you want to input:\n"))
for i in range(0,number):
    yourName=str(input("Enter the names:\n"))
    name=name+[yourName]
print(name)
"""

"""
def main():
    numbers=[]
    sum=0
    try:
        num=int(input("How many numbers do you want to compute:\n"))
        for i in range(0, num):
            myNumbers=int(input("Enter Number "+str(i)+":\n"))
            numbers+=[myNumbers]
            sum+=myNumbers
        print(end="Numbers entered= ")
        for num in numbers:
            print(num ,end=""+",")
        print()
        average=sum/num
        print("Average of",numbers,"is",average)
    except Exception as e:
        print("Only digits are allowed!!!")
        main()
main()
"""
def main():
    myNumber=[]
    num=int(input("How many numbers do you want to compare:\n"))
    for i in range(0,num):
        numbers=int(input("Enter Number "+str(i)+":\n"))
        myNumber+=[numbers]
        theMaximum=max(myNumber)
    print("The maximum of the numbers entered is",theMaximum)
main()