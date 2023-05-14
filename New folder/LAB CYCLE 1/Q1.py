def arithemetic_operations():
	num=int(input("Enter a four digit number:"))
	temp_num=num
	sum=0
	reverse=0                               #reverse to store the reverse number

	rem_1=num%10                        #rem_1- stores the last digit
	reverse=(reverse*10)+rem_1
	num=num//10

	rem_2=num%10                        #rem_2- stores the second last digit
	reverse=(reverse*10)+rem_2
	num=num//10

	rem_3=num%10                        #rem_3- stores the second digit
	reverse=(reverse*10)+rem_3                   
	num=num//10

	rem_4=num%10                        #rem_4- stores the first digit
	reverse=(reverse*10)+rem_4
	num=num//10
	sum=rem_4+rem_3+rem_2+rem_1
	difference=(rem_2*rem_4)-(rem_1*rem_3)
	
	print("Sum=",sum)                        #printing  the sum of the digits
	print("Reverse = ",end="")		  #printing the reverse of the  number
	if(temp_num%10==0):				  
		while(temp_num!=0):
	  		if(temp_num%10==0 and temp_num//10):
	    			print("0",end="")                   
	  		temp_num=temp_num//10
	print(reverse) 
	print("Difference between the product of the digits at 
the odd positions and digits at even position = ",difference)          
                            #printing the difference between the products
	
arithemetic_operations()