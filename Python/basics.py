x,y,z="Python " , "Is " ,"Awesome"
print(x + y + z )

##---------- String ------
First_Name="Alaa"
print (First_Name)
print (f"my name {First_Name} ")
My_Age= 21

##----------Integer-------
print (My_Age)
print (f"my age = {My_Age} years old")

## ----------Complex------
x=3j
print(x)
## ----------Boolean ------
Is_Student =True 
print (Is_Student) 
## ----------Range -------
x=range(6)
print(x)
## ----------Byte---------
x=b"hello"
print(x)
# ##----------------------- Casting --------------------------------
##     type ()  , str () , int()  ,float() ,, bool()


a=11
print (type (a))    ## int
a+=1        ##12 
print (a)

z=str(a)
z+="1"       ## 121 not 13    --concatinat   if i write z=z+1  -> Error
print (z)

name = "blablabla "
bol=bool(name)
print (bol)   ## True
name2= ""
bol2 = bool (name2)  ##false
print (bol2) 


#--------------------------Float /int--------------------------
x=40.0
y=10.0
z=3
g=10
f=2
s=40
print (x/y)     ## float / float -> float 
print (y/z)     ## float / int -> float
print (g/z)     ## int / int -> float
print (g//z)    ## int // int -> int
print (g/f)     ## int /int -> float 
print (s/y)     ## int / float -> float 
print (s//y)    ## int //float -> float
 
#--------------------------input data--------------------------
##  input () : promots user to inter data.  ->  return string 

name = input ("what is your name ")
print (f"hello {name} !")
age = input ("what is your age ")
age = int (age)    ## Must do casting because input return string 
age +=1
print (f"Happy birth day you are {age} years old")
print ("CM²")  ## to make ^2 Numlock + Alt + 0178

#--------------------------Arthematic Operator--------------------------
n= 10
print (n)
n +=1  ## n=n+1
n -=1  ## n=n-1
n *=2   ## n=n*2
n /=2   ## n=n/2
n **=2  ## n=n^2
n %=3   ## n=n%3
print(n)
c=n % 3
print (c) 

#--------------------------basic Math Functions--------------------------
  #round()  -> return 2 decimel or 3 or 4...
  #asb()    -> return positive 
  #pow()    -> return x^n
  #max()    -> return max 
  #min()    -> return min

x=3.14
y=-4
z=5
result1= round(x,1)    # 3.1
result2=abs(y)       #4
result3=pow(4,3)     #64    return int or float
result4= max(x,y,z)  #5
print (result1)
print (result2)
print (result3)
print (result4)

#--------------------------Import  Math--------------------------
import math
x=9.6
y=2
print (math.pi)   ##22/7
print (math.e)
print (math.sqrt(4))  ## 4^2 ->16
print(math.ceil(x))   ##10 
print(math.floor(x)) ##9

#--------------------------IF Statment--------------------------
age= int (input("Enter Your Age :"))
 
if age > 18:
     print("hello")
elif age<18:
     print("no")
elif age ==18:
     print ("yes yes yes ")     
else :
     print ("blblblblb")

for_sale= True

if for_sale:
     print("for sale")
else:
     print ("no sale")   

#--------------------------match case Statment--------------------------
def day_1_2(day):
     match day:
          case 1:
               return "Sunday"
          case 2:
               return "Monday"
          case _ :   # ->  as else ->  if the input value is anything instead 1 or two   , the output will be "Not Valid"
               return "Not valid "
print(day_1_2("blablablabla")) 
print(day_1_2(1))   
print(day_1_2(2))                       


# --------------------------operators--------------------------

operator = input ("enter operator (+,/,*,-,)")

if operator == "+":
 print (5+4)
elif operator=="-":
 print (5-4)
elif operator=="*":
    print ("my favourit operator")
    print (5*4)
elif operator=="/":
    print (5/4)
else:
    print (f"{operator} in not valid")   

#--------------------------logical operator--------------------------
# or  ----- and -----not     

#--------------------------condiditional Expression--------------------------
##codition true  if condition else condition false 
x= 4
y=6
max_number = y if y>x else x
print (max_number)
print ("positive "if x>0 else "negative ")

#---------------------------String Methods--------------------------
##      len()  .find() .rfind()    .capitalize()     .upper()   .lower()     .isalpha() -> true if ther is no any digit or space  
##      .count("")      .replace( , )                .startswith("blbl")   textwrap.fill(string,width)

name = input ("Enter Your Name")
result = len(name)
print (result)
result2 = name.find ("a")
print (result2)
result3= name.rfind("a")
print(result3)
result4=name.upper()
print (result4)
result5=name.capitalize()
print(result5)
result6=name.lower()
print(result6)
print(name.isalpha())
print(name.count("a"))
print (name.replace("E","s"))

import textwrap
string="AlaaAlaaAlaa"
print(textwrap.fill(string,4))  #Alaa
                                #Alaa
                                #Alaa

print(textwrap.wrap(string,4))  #['Alaa','Alaa','Alaa']
#-----(Hackerrank)-----
M,N=(input().split())   #N=3*M -> M odd number   
M=int(M)
N=int(N)

k=(M//2)
for j in range (0,k):
    print((("."+"|"+".")*(2*j+1)).center(N,"-"))
print("WELCOME".center(N,"-"))
for j in range (k-1,-1,-1):
    print((("."+"|"+".")*(2*j+1)).center(N,"-"))
    
 

thickness = 5 #This must be an odd number
c = 'H'

for i in range(thickness):
    print((c*i).rjust((thickness-1)," ")+c+(c*i).ljust((thickness-1)," "))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center((thickness*2)," ")+(c*thickness).center((thickness*6)," "))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center((thickness*6)," ")  )  

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center((thickness*2)," ")+(c*thickness).center((thickness*6)," "))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust((thickness)," ")+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)) 


#--------------------------indexing Operator--------------------------
##-------accessing sequence of elements[start:end:step]

credit_number = "alaa_yasser_elgamal"      
print (credit_number [0])  ## a
print (credit_number[4:6]) ## _y
print (credit_number[:4])  ##alaa
print (credit_number[5:])  ##yasser_elgamal
print (credit_number[::2]) ##aa_asregml
print (credit_number[-1])  ##l  -> the laxt index
print (credit_number[-4:]) ## from index -4 to the last index 
print(credit_number[::-1]) ## reverse 

#--------------------------format specifiers--------------------------
# formate a value based on what flags interested   {value:flags}

price1 = 3000.14159
print(f"price1 is ${price1:.2f}")
print(f"price1 is ${price1:,}")
print(f"price1 is ${price1:+}")
print(f"price1 is ${price1: }")
print(f"price1 is ${price1:,.2f}")

#--------------------------for loop---------------------------
for i in range(0,7) :     # from 0 to 6
   print(i)

for i in range(1,7,2) :     # from 1 to 6 by step 2
   print (i)    # تحت بعض 
   print(i, end=" ")   #  جمب بعض  وبينهم مسافة    

for i in reversed (range(0,7)) :     # from 6 to 0
   print(i)   

name ="alaa "
for x in name:
   #  print (x)
     print (x, end ="")

#--------------------------while--------------------------
i=0
while i<5:
     print(i)
     i+=1

#--------------------------Time--------------------------
import time
my_time=int(input("enter your time"))    ##seconds


for x in range (my_time,0,-1):
  seconds=x%60
  minutes=int(x/60)%60
  hours= int(x/3600)
  print(f"{hours:02} : {minutes:02} : {seconds:02}")
  time.sleep(1)    ## delay 1 second 
  

print ("Time Is UP")  

#------
#--------------------------Data And Time--------------------------
import   datetime   
date=datetime.date(2025,1,2)  
today=datetime.date.today()
time=datetime.time(12,30,0)
now=datetime.datetime.now()
now_format=now.strftime("%H :%M: %S %m -%d -%y")

print(date)
print(today)
print(time)
print(now)
print(now_format)





#--------------------------List--------------------------
# List []  ordered , changeable  and Duplicates OK

fruits=["apple","Banana","Orange","coconut"]

print (fruits[1])
print (fruits[::2])

for x in fruits:
     print (x)
for x in reversed(fruits):
     print (x)  

 #use the list() constructor when creating a new list    
my_list=list(("apple","banan","orange")) 
print(my_list)


fruits=["Apple","Orange","Banana","Banana","Coconut"]
print(fruits[2])      #Banana
print(fruits[-1])     #cocnut
print(fruits[-2])     #Banana
print(fruits[::-1])   #Reverse the list 

fruits[1:3]=["Green","Yellow"]   # change the values of index 1 and index 2
print(fruits)

print (len (fruits))

print(fruits.index("Banana"))

print(fruits.count("Banana"))

print ("Apple" in fruits)    # True OR False   ->True
print ("Pineaple" in fruits)  #-> False



fruits.sort()
print(fruits)

fruits.append("pineaple") # add the item at the end of the list
print(fruits)



fruits.insert(0,"pinaple")  # add the item at specific index 
print(fruits)

fruits.reverse()
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.clear()
print(fruits)

print (dir(fruits))    ## بيجيب ال functions اللي استخدمها مع ال list 
print (help(fruits))     

#--------------------------Set--------------------------
# set{} unordered and immutable but add and remove OK
fruits={"apple","Banana","Banana","Orange","coconut"}      # no duplicates
print (fruits)
fruits.add("Anans")
print(fruits)
#print(dir(fruits))
fruits.remove("apple")
print(fruits)
fruits.pop()
print(fruits)

myset = set()           # Initializing a set
myset = set(['a', 'b']) # Creating a set from a list
print(myset)  #{'a','b'}
myset.add((5,4))
print(myset)   #{'a',(5,4),'b'}

myset.update([1, 2, 3, 4]) # update() only works for iterable objects
print(myset)
myset.update({1, 6}, [5, 13])
print(myset)

#--------------------------COMMON SET OPERATIONS--------------------------
b = {2, 4, 11, 12}
print(a.union(b))        # Values which exist in a or b -> {2, 4, 5, 9, 11, 12}
print(a.intersection(b)) # Values which exist in a and b  -> {2, 4}
print(a.difference(b))   # Values which exist in a but not in b  -> {9, 5}


Mset=set(input().split())
Mset=set(map(int,Mset))
Nset=set(input().split())
Nset=set(map(int,Nset))

DM=Mset.difference(Nset)
for D in DM:
    print(D)
DN=Nset.difference(Mset)
for D in DN:
    print(D)


#-------------------------- Symmetric_difference (Hackerrank Example)--------------------------
M=int(input())
Mset=set(map(int,(input().split())))
N=int(input())
Nset=set(map(int,(input().split())))

symmetric_difference = Mset.symmetric_difference(Nset)
for D in sorted (symmetric_difference):
    print(D)


integer= input().split()
array=list(map(int,input().split())) 
A=set(map(int,input().split()))
B=set(map(int,input().split()))
i=0
for h in array:
    if h in A :
       i+=1
    elif h in B:
       i-=1
print(i)  


#--------------------------Tuple--------------------------
#Tuple() ordered ,unchangeable and Duplicates  FASTER than List

fruits=("apple","Banana","Banana","Orange","coconut")
print(fruits.count("apple"))

#--------------------------IMportant Example using list and multiple inputs --------------------------

my_list=[]
num_Command=int (input("Enter the Number of Commands You Need"))

for i in range (num_Command):
     command_value_index= input("enter the command , value and ((for insert inter)) index ").split()
     command=command_value_index[0]
     if command == "insert":
          value=int (command_value_index[1])
          index=int (command_value_index[2])
          my_list.insert(index,value)
     elif command == "print":
            print(my_list)
     elif command == "remove":
            value = int(command_value_index[1])
            my_list.remove(value)
     elif command == "append":
            value = int(command_value_index[1])
            my_list.append(value)
     elif command == "sort":
            my_list.sort()
     elif command == "pop":
            my_list.pop()
     elif command == "reverse":
            my_list.reverse()
     else:print ("The Command not Valid")    

#--------------------------2D List--------------------------
# 2D list = [list,list,list,........] 

fruit=["apple","orange","banana","coconut"]
vegetable=["carrot","celary","potatoes"]
food=["chicken","fish","turkey"]

groceries=[fruits,vegetable,food]

print (groceries[0])
print (groceries[1][1])

groceries2=[["apple","orange","banana","coconut"],
["carrot","celary","potatoes"],
["chicken","fish","turkey"]]

for collection in groceries2:
  for food in collection:
    print (food, end=(" "))
  print(" ") 


#--------------------------Important Example (Hackerrank)--------------------------
list=[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name,score])
        
sorted_scores = sorted(set(score for _, score in list))  #set of scores in the list
second_lowest=sorted_scores[1]
names=[name for name,score in list if score==second_lowest]
names.sort()
for name in names:
       print(name)

    
#--------------------------Dictionary--------------------------
#dictionary {key:pairs} : ordered and changeable . No Duplicate

capitals ={"USA":"D.C" ,
            "India":"New",
            "China":"Beijing"}


print(capitals.get("USA")) 

capitals.update({"Germany":"Berlin"})     
print(capitals) 

keys=capitals.keys()
print(keys)

value=capitals.values()
print (value)

items=capitals.items()
print(items)

capitals.popitem()
print(capitals.popitem())


for key in capitals:
   print (key)

for key in capitals.keys():
     print (key)

for value in capitals.values():
     print (value)  

for key in capitals:
   print (capitals.get(key))  

for key , value in capitals.items():
     print (f"{key} :{value}")

print(dir(capitals))
print(help(capitals))  

#--------------------------Random--------------------------
import random
games = ("rock","paper","Scissor")
option= random.choice(games)
print (option)

number = random.randint(1,40)
print (number)

rang1=random.randrange(1,40)
print(rang1)
print(help(random))

#--------------------------Function--------------------------

def happy_birth_day(name,year):
     print (f"happy birth day to {name}")
     print (f"you are {year} years old !")

happy_birth_day("alaa",22)     

n = int(input())
for i in range(1,n):
     print (i,end="")


def creat_name ( first , last ):
     first = first.capitalize() 
     last = last.capitalize()

     return first +" "+ last


my_name = creat_name("alaa","yasser")
print (my_name)

#--------------------------default argument--------------------------
#instead to write more argument when calling the function  use default values 
def net_price (list_price,discount=0,tax=.05):
     return list_price *(1-discount) * (1+ tax)

print (f"{net_price(500):.2f}")   #discount=0 and tax=.05 by default
print (net_price(500,.1))         # change the value of discount 
print (net_price(500,.1,.04))     #  change the value of discount and tax 

#--------------------------Keyword argument--------------------------
def hello(graeting, title,first, last ):
     print (f"{graeting} {title}{first} {last}")

hello("Hello","Ms.","Alaa", "Yasser")   ##order for writing argument is important
hello("Hello", first="Alaa",title="Ms.", last="Yasser")   ##order for writing argument is not important
#hello( first="Alaa",title="Ms.", last="Yasser", "Hello")   -> Error   

print ("1","2","3","4", sep="-")   #1-2-3-4
                                                           
#--------------------------Arbitrary--------------------------
"""
* args -> allows you to pass multiple  non_key argumenta
**kwargs -> allows you to pass multiple keyword-arguments
* is unpacking operator
"""

def add_numbers (*args):
     print (type(args))   ## Tuple
     total=0
     for arg in args:
        total+=arg 
     return total

print (add_numbers(1,2,3))
print (add_numbers(1,2,3,4,5,6,7))


def print_address(**kwargs):
      print(type (kwargs))  ## dictionary 
      for value in kwargs.values():
          print (value)

      for key in kwargs:
          print (key)   

      for key, value in kwargs.items():
          print (f" {key}:{value}")      

print_address(street="123 fake st.", city= "Mansoura")

#--------------------------Iterables--------------------------
##Iterables -> An object or collection that can return its elements one at a time ,, allowing it to be iterated over in a loop
numbers =[1,2,3,4]
for number in numbers:
    print (number, end=" ")

print(" ")  
for number in reversed (numbers):
     print (number, end=" ") 
print(" ")  
name = "alaa"
for item in name:
     print (item, end="")

#--------------------------Membership operation--------------------------
#mempership operation -> used to test whether a value or variable is found in a sequence (string ,list, tuple or dictionary)
# in 
# not in
grades={"Alaa":'A',"Sara":'B',"Mohamed":'C'}
student = input ("Enter the Name of The Student ")
if student in grades.keys():
   print (f"the{student}'s grade is {grades.get(student)}")
else :
     print ("This Name Not Found") 

#--------------------------List Comperhension--------------------------
# expression for value in iterable if conditionn
doubles =[x*2 for x in range(1,11)]
print (doubles)    # [2,4,6,8,10,12,14,16,18,20]


fruits=["apple","orange","banana"]
fruits=[fruit.upper() for fruit in fruits]
print(fruits)

grades=[85,42,79,90,56,61,30]
passing_grades=[grade for grade in grades if grade >=60]
print (passing_grades)

name="alaa yasser"
mylist=name.split(" ")
lis=[]
for li in mylist:
     lis.append(li.capitalize())
name=' '.join(lis) 
print(name)    
print(lis)
print(mylist)  # ['alaa','yasser]

#--------------------------Scope resolution--------------------------
# local , Enclosed , Global , Built-in 

def fun(): 
     a=1               # -> Local variable 
     print(a)


def fun1(): 
     a=1
     print(a)
     def fun2():    
          b= 2       # -> Enclosed variable and  the name of this variable must be different (not a) 
          print(b)

x=3 # -> Global variable 


def fun(): 
     global a              # -> global variable   but must call the function before use a as global value
                           #if you want to change a global variable inside a function
                         
     a=1
fun()     
print(a)

from math import e  #  e is Built-in Variable

#--------------------------Exception---------------------------------
#Exception = An Event that interrupts the flow of a program
#            (ZeroDivisionError,TypeError,Value Error) 
#Try => Test the code for Errors       
#Except => Hnadle the Errors
#finally => Run the code 



1+"1"    #TypeError

try:
     number =int( input("Enter a number "))
     print(1/number)
except ZeroDivisionError:   #handle the  ZeroDivisionError 
     print("you can't divide by zero")     
except ValueError:
        print("Enter only numbers please!")  
except Exception:
     print("something wennt wrong!")     

finally:                    #run  the code whatever it is happened 
     print("Do some cleanup here")     
             





#--------------------------bisect-----------------------------
#bisect_left ( , )  -> بيجيب ال index بتاع اول رقم يكون اكبر من او يساوي ال target       -> lower bound 
#bisect_right ( , )  -> بيجيب ال index بتاع اول رقم يكون اكبر من ال target                -> upper bound

import bisect
arr = [1, 2, 4,4,4, 6, 8]
target = 4

# Lower Bound
lower_bound_index = bisect.bisect_left(arr, target) 
print(f"Lower Bound for {target}: {lower_bound_index}")

# Upper Bound
upper_bound_index = bisect.bisect_right(arr, target)
print(f"Upper Bound for {target}: {upper_bound_index}")

#--------------------------multithreading --------------------
#used to perform multiple tasks concurrently
# good for I/O bound tasks like reading files or fetching data from API


import threading
import time

def walk_dog(first,last):
   time.sleep(8)
   print(f"you finish walking the dog{first} {last}")

def  take_out_trash():
   time.sleep(2)

   print("you take out the trash")
def get_mail():
   time.sleep(4)
   print("you get the mail")   

# print(walk_dog())       #wait 8 second then print
# print(take_out_trash()) #wait 2 second then print
# print(get_mail())       #wait 4 seconds then print

chore1 = threading.Thread(target=walk_dog,args=("scooby","Doo"))
chore1.start()

chore2= threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

#you take out the trash   
#you get the mail
#you finish walking the dog

chore1.join()
chore2.join()
chore3.join()
print("All chores completed")

#---HOw to connect to an API using python-----
import requests
base_url="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
   url=f"{base_url}/pokemon/{name}"
   response =requests.get(url)
   print(response)
   
   if response.status_code==200:
      print("Data retruved!")
      pokemon_data=response.json()   # return the data as dictionary
      return pokemon_data
   else :
      print(f"Failed to retrieve data {response.status_code}")   


pokemom_info=get_pokemon_info("pikachu")
if pokemom_info:
   print(f"{pokemom_info["name"]}")
   print(f"{pokemom_info["id"]}")
#----------------------------------------------------------------------------------------------   


print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')






     
          

           

         

  

               
          
   

