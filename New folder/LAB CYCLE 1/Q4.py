#function to print the happy number within range
def happy_number(lower,upper):      #lower-lowerlimit  upper-upperlimit
  count=0
  for i in range(lower+1,upper):
    s=happy(i)                      #invoking happy() function
    if s==1:
      print(i,end=" ")
      count=1                       #count to check whether there is happy number in the range
  print()
  if count==0:                      
    print("There is no happy numbers between this range.")

#function to check whether happy or sad
def happy(n):
  for i in range(1,101):
    sum=0
    while n!=0:
        digit_extr=n%10             #digit_extr-each extracted digits is stored
        square=digit_extr**2                         
        n=n//10                         
        sum=sum+square                         
    n=sum                         
  return (sum)

#Function to print 'n' number of happy numbers
def print_numbers(n):
   count=1                  #count- to check the number of happy numbers printed
   i=1
   while count<=n:
     total=happy(i)                 #invoking happy function
     if total==1:                   #total- conditional variable
        print(i,end=" ")
        count+=1
     i=i+1
   print('') 

#function to invoke all of the above mentioned functions 
def main():
  print("\t HAPPY NUMBER FINDER")
  num=int(input("Enter the number to check:"))
  if happy(num)==1:
    print("Its a Happy number.")
  else:
    print("Its a Sad number.")
  print("\tHappy numbers within a range.")
  lowerlimit=int(input("Enter the Lower limit:"))
  upperlimit=int(input("Enter the Upper limit:"))
  happy_number(lowerlimit,upperlimit)   
  print("\tFirst N happy numbers") 
  N=int(input("Enter the number of terms:"))
  print_numbers(N)                   #N-number of terms to print

main()                              #invoking main function