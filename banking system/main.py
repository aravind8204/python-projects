import backend
import random

i=1
while(i==1):
    print("\t\t======== STAR BANK ========\t\n")
    print("\t1.Create new account")
    print("\t2.View account")
    print("\t3.Update account")
    print("\t4.Debit")
    print("\t5.Credit")
    choice=int(input("Enter your option : "))
    match(choice):
        case 1:
            lis=[]
            name=input("Enter name: ")
            mobile=int(input("Enter mobile number: "))
            email=input("Enter Email ID: ")
            addr=input("Enter address: ")
            pin=int(input("Enter 4 digit pin for your account: "))
            amount=int(input("Enter initial amount: "))
            accno=random.randrange(1000000000000,9999999999999)
            acnos=backend.fetch_acno()
            for i in range(0,len(acnos)):
                lis.append((acnos[i])[0])
            if(accno not in lis):
                backend.new_acc(str(accno),name,mobile,email,addr,pin)
                backend.debit(str(accno),pin,"initial amount",amount)
                print("Amount deposited..\n\nYour A/C number is",accno)
            else:
                break
            break
        case 2:
            ac2=input("Enter A/C number: ")
            pin1=int(input("Enter pin: "))
            r=backend.view(ac2,pin1)
            print("\nDetails-\nName: ",(r[0])[0],"\nMobile Number: ",(r[0])[1],"\nEmail ID: ",(r[0])[2],"\nAddress: ",(r[0])[3],"\nCurrent Balance: ",r[1])
            break
        case 3:
            ac2=input("Enter A/C number: ")
            pin1=int(input("Enter pin: "))
            r=backend.view(ac2,pin1)
            print("Old details...")
            print("\nDetails-\nName: ",(r[0])[0],"\nMobile Number: ",(r[0])[1],"\nEmail ID: ",(r[0])[2],"\nAddress: ",(r[0])[3],"\nCurrent Balance: ",r[1])
            print("\n\nUpdate the details..")
            n=input("Enter name: ")
            m=int(input("Enter mobile number: "))
            e=input("Enter Email: ")
            ad=input("Enter address: ")
            backend.acc_update(n,m,e,ad,ac2)
            print("Update successfully....")
            break
        case 4:
            ac1=int(input("Enter A/C number: "))
            pin=int(input("Enter 4 digit pin for your account: "))
            de=input("Enter description of the transaction: ")
            am=int(input("Enter amount: "))
            try:
                backend.debit(str(ac1),pin,de,am)
                print("Amount deposited....")
            except:
                print("please enter correct details")
            break
        case 5:
            ac1=int(input("Enter A/C number: "))
            pin=int(input("Enter 4 digit pin for your account: "))
            de=input("Enter description of the transaction: ")
            am=int(input("Enter amount: "))
            try:
                backend.credit(str(ac1),pin,de,am)
                print("Amount Credited....")
            except:
                print("please enter correct details")
            break
        case default:
            break


