"""
#reverse a string
str=str(input("enter a string:"))
i=1
con=""
while (i<=len(str)):
 u=str[len(str)-i]
 con=con+u
 i=i+1
print(con)


#greatest of 3 numbers
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
#x=[a,b,c]
#print(max(x))    
if(a>b and a>c):
    print(a," is the greatest number")              
elif (b>a and b>c):
    print(b,"is the greatest number")
else:
    print(c,"is the greatest number")

#count vowels in string
str=str(input("enter a string:"))
x=["a","e","i","o","u"]
i=0
for el in str:
    if el in x:
        i+=1
        
print("there are",i," vowels in the string")

#getting the square of all the elements and inserting it in a list
list=[1,2,3,4,5,6,7,8,9,10]
new=[]
for i in list:
    x=i**2
    new.append(x)
print(new)


#Build a student record system using dictionary (name, age, marks)
record={"abbas":{"age":18,"marks":67},
        "nitoo":{"age":19,"marks":91},
        "sanjay":{"age":28,"marks":82},
        "nuba":{"age":12,"marks":89},
        "saumya":{"age":55,"marks":36},
        }

print(record["abbas"])



#prime or not
def prime(x):
    a=2
    while x%a!=0:
        a+=1
    if a==x:
        print("prime")
    else:
        print("not prime")

prime(64)





#Contact book (add, search, delete contacts using dictionary)

contacts={"abbas":9702450406,
          "nitu":8600479086,
          "sanjay":9998464331}

options="1.add \n2.search \n3.delete \n4.show directory \n5.exit \n"
print(options)


while True:
    select=int(input("select an operation:"))

    if select==1:
        name=str(input("enter the name:"))
        number=int(input("enter the number:"))
        contacts[name]=number
        print(name,"is succesfully added in the contacts \n")
        
    elif select==2:
        search=str(input("enter the name:"))
        print(contacts[search])

    elif select==3:
        delete=str(input("enter the name:"))
        contacts.pop(delete)
        print(delete,"is succesfully deleted from the contacts \n")

    elif select==4:
        for key,value in contacts.items():
           print(f"{key}:{value}")

    elif select==5:
        print("program stopped \n") 
        break
    
    else:
        print("Please enter a valid operation")


"""    


#ATM simulation (deposit, withdraw, balance using functions)

balance=10000

def show_balance():
    global balance
    print("Your balance is",balance,"Rs")

def deposit(amount):
    global balance
    balance = balance + amount
    print("you have deposited",amount,"")

def withdraw(amount):
    global balance
    balance=balance-amount
    print("you have withdrawn",amount,"Rs")

show_balance()
deposit(500)
show_balance()