def sort_merge(temp1,temp2):                         #function to merge and sort the list
   list_final=temp1+temp2
   list_final.sort()
   return list_final
   
def final_sort(l1,l2):                               #function to sort the individual list
   l1.sort()
   l2.sort()
   final_list=sort_merge(l1,l2)
   print("5. Single Sorted list         :",final_list)
   print("_"*70,"\n")
   
def function(l):                             #function to evaluate the mathematical function
   l_function=[]                             # l_function - list of result of the expression
   for i in range(0,len(l)):                 #��(��) = ��^2 – ��
      l_function.append(l[i]**2 -l[i])
   print("4. Values of functions        :",l_function)
   final_sort(l,l_function)
   
def duplication(l):                        #function to rewrite the list without duplication
   l_ndupli=tuple(set(l))
   l_ndupli=list(l_ndupli)
   print("3. List without duplication   :",l_ndupli)
   function(l_ndupli)

def list_tuple(l):                           #function to convert the list to tuple
   l_tuple=tuple(i for i in l)
   print("2.Tuple by list Comprehension :",l_tuple)
   duplication(l_tuple)

def rotate(l):                                #function to rotate the list
   n= int(input("\n1. Enter Number of rotation: "))
   temp=[]

   if n>len(l):                               #Condition to avoid repeated looping
      n = int(n%len(l))   
   for i in range(len(l)-n,len(l)):
     #print(len(l),n,i)
     temp.append(l[i])
   for i in range(0,len(l)-n):
     temp.append(l[i])
   print("\tRotated List          :",temp)
      
def main():                                               #main function to get the list
   l_string=[]
   print("\n\tList of String to list of Integers and operations.")
   print("_"*70)
   l_string=input("Enter Numbers separated by space : ")      #l_string - list of string 
   l_string=list(l_string.split(" "))                         
   print("\nList of string   :",l_string)
   l_int=[]                                                   #l_int - list of integers
   for i in l_string:
      l_int.append(int (i))
   print("List of Integers :",l_int)
   print("_"*70)
   rotate(l_int)                                              #function call
   list_tuple(l_int)                                          #function call
  
main()                                                        #program execution