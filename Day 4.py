"""
#Write a program to append text to a file
f=open("C:\\Users\\abbaz\\Desktop\\python docs\\TrialTextFile.txt","a")
f.write("\n Optimus prime")
f.close()


#Read contents of a file and print them
x=open("C:\\Users\\abbaz\\Desktop\\python docs\\TrialTextFile.txt","r")
print(x.read())
x.close()



#3. Use math to calculate factorial of a number
import math
print("The factorial of the entered number will be",math.factorial(int(input("enter a number:"))))


#Use random to generate a random number between 1-10
import random
print(random.randint(1,10))



#Expense Tracker (Beginner version) → Add expenses, view total, save to file

while True:
 choice=str(input("Press A to add an expense OR press V to view your expenses..!"))
 x=choice.lower()

 if x=="a":
    record=open("C:\\Users\\abbaz\\Desktop\\python docs\\exptrack.txt","a")
    e=str(input("enter the name of the month:")) 
    b=int(input("enter rent amount:"))
    c=int(input("enter water bill:"))
    d=int(input("enter groceries expense:"))

    newdata=(f" \n \n{e} \nrent:{b}, \nwater: {c}, \ngroceries:{d}, \nTotal:{b+c+d}")
    record.write(newdata)
    print("Added",e ,"expense in the record")
    record.close()

 elif x=="v":
    record=open("C:\\Users\\abbaz\\Desktop\\python docs\\exptrack.txt","r")
    print(record.read())
    record.close()

 else:
   print("please enter a valid option")

   
#Quiz Game → Ask questions, count score, save results in a file

name=str(input("whats your name son:"))
print("Swagaat hai aapka",name," kaun banega crorepati mai!!! \n"\
      "ye raha pehla sawal aapki screen pr \n")
points=0


one=str(input("Which animal is the fastest land creature? \n"
              ))
if one.lower()=="cheetah":
    print("correctoh \n")
    points+=12.5
else:
    print("Wrong...Son the correct answer is cheetah \n")


two=str(input("Which animal uses echolocation to navigate and locate prey? \n"
              ))
if two.lower()=="bat":
    print("sahi jawaab \n")
    points+=12.5
else:
    print("galat jawab ...The correct answer is bat \n")


three=str(input("What is the largest animal in the world? \n"
              ))
if three.lower()=="elephant":
    print("Rightoh!! \n")
    points+=12.5
else:
    print("no son the sahi jawaab is elephant \n")


four=str(input("What is the largest animal in the ocean? \n"
              ))
if four.lower()=="whale":
    print("sahi jawaab \n")
    points+=12.5
else:
    print("galat jawab ...The correct answer is whale \n")


five=str(input("How many arms does a squid have? \n"
              ))
if five.lower()=="10":
    print("yes sirrr you are right!! \n")
    points+=12.5
else:
    print("Naah son ...The  answer is 10 \n")


six=str(input("What is the largest living bird? \n"
              ))
if six.lower()=="ostrich":
    print("lessgooo...ostrich is the right answer \n")
    points+=12.5
else:
    print("naaah naaah naaah its ostrich")


seven=str(input("How many eyes does a caterpillar have? \n"
              ))
if seven.lower()=="12":
    print("12 sahi uttar hai ...shabbaash \n")
    points+=12.5
else:
    print("galat uttar , sahi jawab hai 12 \n")


eight=str(input("Which bird is the only one capable of flying backward? \n"
              ))
if eight.lower()=="hummingbird":
    print("hummingbird is the correct answer \n")
    points+=12.5
else:
    print("its hummingbird dumbo \n")


print("Congrats son.....Your total points is",points)

save=open("C:\\Users\\abbaz\\Desktop\\python docs\\QuizoResulto.txt","a")

save.write(f" \n{name}:{points} points")
print("data saved in the file")
save.close()
"""

#To-Do List App → Add tasks, view tasks, mark done, save in file
i=0
def add_task():
    to_do_file=open("C:\\Users\\abbaz\\Desktop\\python docs\\to_do_file.txt","r")
    global i
    i+=1
    to_do_file=open("C:\\Users\\abbaz\\Desktop\\python docs\\to_do_file.txt","a")
    task=str(input("Please enter a task: "))
    status="pending"
    to_do_file.write(f" \n{i}. {status} : {task}")
    to_do_file.close()
    print("Task added successfully")

def view_tasks():
    to_do_file=open("C:\\Users\\abbaz\\Desktop\\python docs\\to_do_file.txt","r")
    print(" \n \n-------TASKS-------")
    print(to_do_file.read())

def mark_done():
    file= open("C:\\Users\\abbaz\\Desktop\\python docs\\to_do_file.txt","r")
    file.readline()
    idx=str(input("enter the task:"))
    for line in file:      
        if line[0]==idx:
            y=line.replace("pending","completed")
            print(y)
    for line in file:
                print(line)


                    
            

print("1.Add task \n2.view tasks \n3.mark done \n4.exit")
while True:
    select=int(input("select an option:"))

    if select==1:
        add_task()
    elif select==2:
        view_tasks()
    elif select==3:
        mark_done()
    else:
        print("program stopped")
        break
    
  

 