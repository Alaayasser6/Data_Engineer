#--------------------------file detection---------------------------
import os   # way for python to interact with the operating system

file_path= "test.txt"


if os.path.exists(file_path):
    print(f"The location {file_path} exists")
    if os.path.isfile(file_path):
        print("That is a file ")


else :
    print("The location doesn't exist")    
    

#--------------------------python writing files(.txt,.json,.csv)--------------------------
txt_data="I like pizza!"
file_path="output.txt"   #created on the same directory 

try:

 with open(file=file_path,mode="x") as file:  #mode= w : is for write   , mode = x to write file if that file doesn't exist , mode=a to append any new data will be appended on that file  
     file.write(txt_data)
     print(f"txt file {file_path} is created")
except FileExistsError:
   print("that file already exists")

#----
#write json
import json
employee={"name":"spingebob",
          "age":30,
          "job":"cook"
          }

file_path="output.json"   #created on the same directory 

try:

 with open(file=file_path,mode="w") as file:  #mode= w : is for write   , mode = x to write file if that file doesn't exist , mode=a to append any new data will be appended on that file  
     json.dump(employee,file,indent=4)
     print(f"json file {file_path} is created")
except FileExistsError:
   print("that file already exists") 

#------

import csv

employee=[["Names","Age","job"],
          ["Spongebob",30,"Cook"],
          ["Patrick",37,"Unemployee"]]


file_path="output.csv"   #created on the same directory 

try:

 with open(file=file_path,mode="w",newline="") as file:  #mode= w : is for write   , mode = x to write file if that file doesn't exist , mode=a to append any new data will be appended on that file  
     writer=csv.writer(file)
     for row in employee:
        writer.writerow(row)
     print(f"csv file {file_path} is created")
except FileExistsError:
   print("that file already exists") 


#--------------------------Read Files--------------------------
#   txt 

file_path="output.txt"
try :
   with open (file_path,mode="r") as file:
      content = file.read ()
      print(content)
except FileNotFoundError:
   print("That file was not found") 

#   json 
import json  
file_path="output.json"
try :
   with open (file_path,mode="r") as file:
      content = json.load((file))
      print(content)
except FileNotFoundError:
   print("That file was not found")  

#   csv 
import csv 
file_path="output.csv"
try :
   with open (file_path,mode="r") as file:
      content = csv.reader((file))
      for line in content:
        print(line)
except FileNotFoundError:
   print("That file was not found") 


   
   


