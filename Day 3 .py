
"""
#Create a class Car with attributes brand and year
class car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year


corolla=car("toyota",2022)
taycan=car("porsche",2025)

print(corolla.brand)
print(taycan.year)





#Create a class Circle with methods for area & perimeter
class circle:
    def __init__(self,circle_name):
        self.circle_name=circle_name
    
    #methods

    def Area(self,radius):
        x=3.1415*(radius**2)
        print("The area of the ",self.circle_name,"  will be",x,"sq.cms")

    def peri(self,radius):
        y=2*3.1415*radius
        print("The perimeter of the ",self.circle_name," will be",y,"cms")

       


e=circle("king circle")
f=circle("thick circle")

circle.Area(f,9)
circle.peri(e,7)


#Write a try-except block to handle division by zero

try:  
    number=int(input("enter a number to find the inverse of that number: "))
    x=1/number
    print(x)

except ZeroDivisionError:
    print("inverse of zero doesn't exist")

    

#· Class BankAccount with deposit, withdraw, balance methods

class BankAccount:
    def __init__(self,Account_name,saving):
        self.Account_name=Account_name
        self.saving=saving

    def balance(self):
        print("you have a balance of ",self.saving,"Rs")

    def deposit(self,amount):
        self.saving+=amount
        print(amount,"Rs is deposited in your account (Account name: ",self.Account_name,")")
        print("now your total balance will be",self.saving,"Rs")

    def withdraw(self,amount):
        self.saving-=amount
        print(amount,"Rs is withdrawn from your account (Account name :",self.Account_name,")")
        print("now your total balance will be",self.saving,"Rs")

acc1=BankAccount("nitoo",10000)
BankAccount.balance(acc1)
BankAccount.deposit(acc1,200)

acc2=BankAccount("sanjay",35000)
BankAccount.balance(acc2)
BankAccount.withdraw(acc2,15000)



#· Extend with SavingsAccount that calculates interest

class BankAccount:
    def __init__(self,Account_name,saved,Account_type):
        self.Account_name=Account_name
        self.saved=saved
        self.Account_type=Account_type

    def balance(self):
        print("you have a balance of ",self.saved,"Rs")

    def deposit(self,amount):
        self.saved+=amount
        print(amount,"Rs is deposited in your account (Account name: ",self.Account_name,")")
        print("now your total balance will be",self.saved,"Rs")

    def withdraw(self,amount):
        if self.Account_type=="saving account":
            x=self.saved- amount
            if x>5000:
                 self.saved-=amount
                 print(amount,"Rs is withdrawn from your account (Account name :",self.Account_name,")")
                 print("now your total balance will be",self.saved,"Rs")
            else :
                 print("its a saving account , you cant withdraw if your balance is 5000 Rs")
        elif self.Account_type=="non saving account":
            self.saved-=amount
            print(amount,"Rs is withdrawn from your account (Account name :",self.Account_name,")")
            print("now your total balance will be",self.saving,"Rs")
        
        else:
            print("account type not defined")
        
    def interest(self,years,rate=0.05):
        int_ammount=self.saved*rate*years
        print("The total interest after",years,"years will be ",int_ammount,"Rs")



acc1=BankAccount("abbas",10000,"Saving account")
BankAccount.balance(acc1)
BankAccount.withdraw(acc1,3000)
BankAccount.interest(acc1,3)



acc2=BankAccount("saumya",20000,"saving account")
BankAccount.balance(acc2)
BankAccount.deposit(acc2,5000)
BankAccount.withdraw(acc2,19000)
BankAccount.interest(acc2,4)
"""

#Student grade manager (take marks, calculate grade, store in dictionary)  
           

record={
    "abbas":{"marks":73,
            "grade":"C"},
    "sanjay":{"marks":86,
            "grade":"B"}
}

options="1.add \n2.show \n3.exit"
print(options)

while True:
 select=int(input("select an option:"))

 if select==1:
    name=str(input("enter the name:"))
    marks=int(input("enter the marks:"))

    if marks<100 and marks>=90:
      grade="A"
    elif marks<90 and marks>=80:
      grade="B"
    elif marks<80 and marks>=70:
      grade="C"
    elif marks<70 and marks>=60:
      grade="D"
    else:
      grade="E"


    record[name]={"marks":marks,
                  "grade":grade}
    print("successfully added",name,"in the dictionary \n")

 elif select==2:
   for key,value in record.items():
     print(f"{key}:{value}")

 elif select==3:
  print("program stopped")
  break
 else:
   print("please enter a valid option")









