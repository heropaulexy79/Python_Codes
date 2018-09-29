'''
Author:Heropaulexy
Date: 18th August 2018
Program to print all prime numbers
'''

'''
Numbers=[]
primeNumbers=[]
nonPrime=[]
for i in range(0,500):
    Numbers+=[i]
    if i%2==0:
        nonPrime+=[i]
#nonPrimes=500*[False]
    else:
        primeNumbers+=[i]
print("The numbers are",Numbers)
print("The Odd Numbers are",primeNumbers)
print("The Even Numbers are",nonPrime)
'''
max=200
nonprimes=max*[False]
#print(nonprimes)
nonprimes[0]=nonprimes[1]=True
for i in range(2,max+1):
    if not nonprimes[i]:
        print(i,end="")
        for j in range(2*i,max+1,i):
            nonprimes[j]=True