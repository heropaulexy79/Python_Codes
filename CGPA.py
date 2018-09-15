#Author: heropaulexy
#Date: 17th August 2018
#Program that calculates G.P.A

from decimal import Decimal
import math

print("--------------------------------------------------------------------------------------")
print("=====================WELCOME TO G.P.A CALCULATOR======================================")
name=input("Enter your full name:")
print("WELCOME",name)
print("**************************************************************************************")
noc=0
totalunit=0
totalgpa=0
courses=int(input("How many courses are you offering:"))
while noc<courses:
    course_code=input("Enter Course Code:")
    unit=float(input("Enter Course Unit:"))
    gp=float(input("Enter G.P.A:"))
    totalunit=math.floor(totalunit+unit)
    gpa=unit*gp
    totalgpa=math.floor(totalgpa+gpa)
    noc +=1
    if totalunit>24:
        print("Dear,",name,"The maximum unit for a semester is 24")
    else:
        cgpa=Decimal(totalgpa/totalunit)
        CGPA=round(cgpa,2)
        if CGPA>=4.5:
            print("Dear,",name,"Your C.G.P.A is",CGPA)
            print("You are a shinning star, You can do better")
        elif CGPA>=3.5 and CGPA<4.5:
            print("Dear,", name, "Your C.G.P.A is", CGPA)
            print("You can do better, There is room for improvement")
        elif CGPA>=2.5 and CGPA<3.5:
            print("Dear,", name, "Your C.G.P.A is", CGPA)
            print("There is more you can do than this")
        elif CGPA>=1.5 and CGPA<2.5:
            print("Dear,", name, "Your C.G.P.A is", CGPA)
            print("Dear, do all you can do reach the top")
        else:
            print("Dear,", name, "Your C.G.P.A is", CGPA)
            print("You are not a good standing")
print("==============================================================================================================================================")
print("============================================================= NAME:",name,"============================================================")
print("=================================================================== C.G.P.A:",CGPA,"============================================================")
print("===============================","Total G.P.A =",totalgpa,"========================================","Total unit =",totalunit,"====================================")