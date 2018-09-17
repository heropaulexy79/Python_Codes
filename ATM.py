#Author:heropaulexy
#30th August 2018
#AN ATM Program
"""""
name=input("Please enter your name:\n")
if name.isalpha():
    print("Dear",name,", Welcome to our Automated Teller Machine....")
"""

def main():
    initialBalance = 1000
    newBalance = 0000
    try:
        try:
            pin=0000
            myPin =int(input("Please input your pin, default pin is 0000\n"))
        except Exception as e:
            print("Only digits are allowed!!!")
        if pin==myPin:
                print("******************************************************************************************")
                print("1. Withdrawal                 2. Deposit                      3. Airtime top-up")
                print("4. Check Balance              5. Change Pin")
                option=int(input("Please choose your option\n"))
                if option==1:
                    print("1. 1000          2. 2000             3.5000")
                    print("4. 10000         5. 20000            6.Other")
                    withdraw=int(input("Choose your option below\n"))
                    if withdraw>initialBalance:
                        print("Dear, Insufficient funds!!!")
                    elif withdraw==1:
                        print("You have successfully withdrawn an amount of #1000 from your account")
                        print("Do you want to perform another transaction?")
                        transaction = int(input("1. YES           2. NO"))
                        if transaction == 1:
                            main()
                        else:
                            print("Thanks for banking with us...")
                    elif withdraw==2:
                        print("You have successfully withdrawn an amount of #2000 from your account")
                        print("Do you want to perform another transaction?")
                        transaction = int(input("1. YES           2. NO"))
                        if transaction == 1:
                            main()
                        else:
                            print("Thanks for banking with us...")
                    elif withdraw==3:
                        print("You have successfully withdrawn an amount of #5000 from your account")
                        print("Do you want to perform another transaction?")
                        transaction = int(input("1. YES           2. NO"))
                        if transaction == 1:
                            main()
                        else:
                            print("Thanks for banking with us...")
                    elif withdraw==4:
                        print("You have successfully withdrawn an amount of #10000 from your account")
                        print("Do you want to perform another transaction?")
                        transaction = int(input("1. YES           2. NO"))
                        if transaction == 1:
                            main()
                        else:
                            print("Thanks for banking with us...")
                    elif withdraw==5:
                        print("You have successfully withdrawn an amount of #20000 from your account")
                        print("Do you want to perform another transaction?")
                        transaction = int(input("1. YES           2. NO"))
                        if transaction == 1:
                            main()
                        else:
                            print("Thanks for banking with us...")
                    elif withdraw==6:
                        myWithdraw=str(input("Enter your desired amount\n"))
                        if myWithdraw.isdigit():
                            print("You have successfully withdrawn an amount of #",myWithdraw)
                            print("Do you want to perform another transaction?")
                            transaction=int(input("1. YES           2. NO\n"))
                            if transaction == 1:
                                main()
                            else:
                                print("Thanks for banking with us...")
                        else:
                            print("Please enter digits only!!!")
                    elif option==2:
                            deposit=int(input("How much do you want to deposit?\n"))
                            print("You have successfully deposited an amount of",deposit,"into your account")
                            newBalance=deposit+initialBalance
                            print("Do you want to perform another transaction?")
                            transaction = int(input("1. YES           2. NO\n"))
                            if transaction == 1:
                                main()
                            else:
                                print("Thanks for banking with us...")

                    elif option==3:
                            print("Choose your operator below")
                            print("1. MTN              2. Airtel            3. Glo")
                            print("4. Etisalat         3. Visaphone         5. Others")
                            operator=int(input("Choose your option below\n"))
                            if operator==1:
                                mobileNo=int(input("Please enter your phone number\n"))
                                amount=int(input("Enter desired amount\n"))
                                print("Airtime of",amount,"has just been credited to",mobileNo)
                                print("Do you want to perform another transaction?")
                                transaction = int(input("1. YES           2. NO\n"))
                                if transaction == 1:
                                    main()
                                else:
                                    print("Thanks for banking with us...")
                            elif operator==2:
                                mobileNo = int(input("Please enter your phone number\n"))
                                amount = int(input("Enter desired amount\n"))
                                print("Airtime of", amount, "has just been credited to", mobileNo)
                                print("Do you want to perform another transaction?")
                                transaction = int(input("1. YES           2. NO\n"))
                                if transaction == 1:
                                    main()
                                else:
                                    print("Thanks for banking with us...")
                            elif operator==3:
                                mobileNo = int(input("Please enter your phone number\n"))
                                amount = int(input("Enter desired amount\n"))
                                print("Airtime of", amount, "has just been credited to", mobileNo)
                                print("Do you want to perform another transaction?")
                                transaction = int(input("1. YES           2. NO\n"))
                                if transaction == 1:
                                    main()
                                else:
                                    print("Thanks for banking with us...")
                            elif operator==4:
                                mobileNo = int(input("Please enter your phone number\n"))
                                amount = int(input("Enter desired amount\n"))
                                print("Airtime of", amount, "has just been credited to", mobileNo)
                                print("Do you want to perform another transaction?")
                                transaction = int(input("1. YES           2. NO\n"))
                                if transaction == 1:
                                    main()
                                else:
                                    print("Thanks for banking with us...")
                            elif operator==5:
                                mobileNo = int(input("Please enter your phone number\n"))
                                amount = int(input("Enter desired amount\n"))
                                print("Airtime of", amount, "has just been credited to", mobileNo)
                                print("Do you want to perform another transaction?")
                                transaction = int(input("1. YES           2. NO\n"))
                                if transaction == 1:
                                    main()
                                else:
                                    print("Thanks for banking with us...")
                    #elif option==4:
                        #balance=newBalance
                        #print("Dear Customer, Your balance is",balance)
                    elif option==5:
                        oldPin=int(input("Please enter your current password\n"))
                        if oldPin==myPin:
                            newPin=int(input("Please enter your new password\n"))
                            pin=int(input("Confirm the new password\n"))
                            if newPin==pin:
                                myPin=pin
                            else:
                                print("Passwords does not match")
                        else:
                            print("Incorrect Password!!!")
                        print("Do you want to perform another transaction?")
                        transaction = int(input("1. YES           2. NO\n"))
                        if transaction == 1:
                            main()
                        else:
                            print("Thanks for banking with us...")

        else:
            print("Incorrect Password.......")
            print("***********************************************************************************************")
    except Exception as e:
        print(e)
    main()

main()