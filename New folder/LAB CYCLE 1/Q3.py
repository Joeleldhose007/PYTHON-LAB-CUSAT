#function to include the details of the employee
def get_detail():
  name=str(input("Enter the name \t  : "))
  code=int(input("Enter the code \t  : "))
  basic_pay=float(input("Enter the basic pay:"))
  return (name,code,basic_pay)

#function to calculate the Gross Salary
def gross_salary(bp,da,hra,ma):
  gs=bp+da+hra+ma                              #gs- Gross Salary value
  return gs

#function to claculate Deduction
def deduction(pt,pf,it): 
  print("Professional Tax         :",pt)
  print("Provident Fund           :",pf,"%")
  print("Income Tax               :",it,"%")             
  d=pt+pf+it                                   #d- Deduction value
  print("Deduction              =  ",d)
  return d

#function to calculate the Net Salary
def net_salary(BP,DA,HRA,MA,PT,PF,IT):
  print("Dearness Allowance       :",DA,"%")
  print("House Rent Allowance     :",HRA,"%")
  print("Medical Allowance        :",MA)
  GS=gross_salary(BP,DA,HRA,MA)                #invoking the function gross_salary and return value to GS
  D=deduction(PT,PF,IT)                        #invoking the function deduction and return value to D
  print("Gross salary           =  ",GS)
  net_sal=  GS-D                                    #net_sal- store value of Net Salary
  print("Net Salary             =  ",net_sal)

#function to display the input details of employee
def display(nam,cod,basic_pay):                 #nam-name   cod-code   
  print("Name of the employee \t :",nam)
  print("Code of the employee \t :",cod)
  print("Basic pay of the employee:",basic_pay)

#function from which all other functions are invoked
def main():
  print("Enter the details of the employee.")
  n,c,bp=get_detail()                             #n-name   c-code      bp-Basic Pay of the employee
  print("\tPay list")
  display(n,c,bp)                             #invoke Display function
  if(bp<10000):
    net_salary(bp,5,2.5,500,20,8,0)           #invoke net_salary function
  elif(bp<30000 and bp>=10000):
    net_salary(bp,7.5,5,2500,60,8,0)
  elif(bp<50000 and bp>=30000):
     net_salary(bp,11,7.5,5000,60,11,11)
  else:
    net_salary(bp,25,11,7000,80,12,20)

main()                        #invoking the main function