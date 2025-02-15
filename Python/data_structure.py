
#------------
 
 #-------------------------Linear Search------------------------------------
i=6
count=0
my_list=[1,2,3,4,5,7,8]                                    #count =1
while count < len(my_list) and (my_list[count] != i):      # for j in my_list :
                                                           #    if j != i:
                 count+=1                                          #       count +=1
                                                           #     else :
                                                           #        break
if count < len(my_list):  # len -> 7  and count can't reach the 7 أخره6
     print(count)
else:
  print("The number Is Not In The List")   
  #---------------------------Binary Search----------------------------------
import math
i=19
my_list=[1,2,5,7,8,9,20,21,25] 
min=0
max=len(my_list)-1 
mid=math.floor((min+max)/2) 
while i != my_list[mid] and max>=min:
     print("i will not Exist")

     if i>my_list[mid]:
          min=mid+1
     elif i <my_list[mid]:
          max=mid-1
     mid=math.floor((min+max)/2)     
if max<min:
     print("Not Exist")
else :
     print(mid)    

#------------------------------sort then search------------------------------------------
import math
def sort(list):
     n=len(list)-1
     for i in range(n) :
          for j in range(n-i):
               if list[j]>list[j+1]:
                    list[j] , list[j+1] = list[j+1] , list[j]
     return list

def binary_search(list,i):
     min=0
     max=len(my_list)-1 
     mid=math.floor((min+max)/2) 
     while i != my_list[mid] and max>=min:
       if i>my_list[mid]:
          min=mid+1
       elif i <my_list[mid]:
          max=mid-1
       mid=math.floor((min+max)/2)     
     if max<min:
         return -1
     else:
         return mid   
     

my_list =[14,15,16,3,4,5]
sorted_list=sort(my_list)
location=binary_search(sorted_list,16)
print (f"sorted list = {sorted_list}")
if location==-1:
     print("Number doesn't Exist")
else:
     print(f"Location = {location}")