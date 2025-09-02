"""
#1. Print your name, age, and favourite hobby
name="abbaz"
age=22
hobby="photography"

print("Hi my name is",name,"i'm",age,"yrs old and my favourite hobby is",hobby)


#2. Take two numbers and print their sum
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))

print("Sum of the 2 numbers will be",a+b)

#3. Swap two numbers without using a third variable
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
(a,b)=(b,a)
print (a,b)



#4. Check if a number is even or odd
a=int(input("please enter a number:"))
b=a%2
if b==1:
    print(a," is an odd number")
else:
    print(a," is an even number")


#Program to calculate area & perimeter of rectangle, circle, triangle

print("1. rectangle\n"\
      "2. circle\n"\
      "3. traingle"
    )

select=int(input("select a shape:"))

if select==1:
    x=int(input("enter the length of smaller side:"))
    y=int(input("enter the length of larger side:"))
    a=2*(x+y)
    b=x*y
    print("the area of the rectangle will be",b,"sq.cms and the perimeter will be",a,"cm")

elif select==2:
    x=int(input("enter the radius of the circle:"))
    a=3.14159*((x)**2)
    b=2*3.14159*x
    print("the area of the circle will be",b,"sq.cms and the perimeter will be",a,"cm")

elif select==3:
    x=int(input("enter the base of the triangle:"))
    y=int(input("enter the height of triangle:"))
    a=(x*y)/2
    b=(x+y)+((x**2)+(y**2))**(1/2)
    print("the area of the triangle will be",b,"sq.cms and the perimeter will be",a,"cm")

else :
    print ("please enterm a valid option")


"""
#mini calculator

a=float(input("enter the first number:"))  
print("  +  ,  -  ,  *  ,  /  ")
z= input("select an operator:")

b=float(input("enter the second number:"))

if z=="+":
    print(a+b)
elif z=="-":
    print(a-b)
elif z=="*":
    print(a*b)
elif z=="/":
    print(a/b)
else :
    print (" please enter a valid option")


"""
#simple interest
def simple_interest():
    P=int(input("enter your principal amount:"))
    I=float(input("enter your interest rate:"))
    T=float(input("enter your duration of investment in years:"))

    S=P*I*T
    print("The SI on the principal amount ",P," will be",S)

  

#compound interest

def compound_interest():
    P=int(input("enter your principal amount:"))
    I=float(input("enter your interest rate:"))
    T=float(input("enter your duration of investment in years:"))
    n=12 #no. of times interest is getting compounded per year

    A=P*(1+(I/n))**(n*T)  

    print ("Your compounded interest after",T, "year will be ",A)

"""