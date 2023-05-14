import random

class Box:                                #creating class named box
   length=0
   breadth=0
   height=0
   area=0
   volume=0
   r1=0
   r2=0
   r3=0
   total=0

   def __init__(self,length,height,breadth):
    self.length=length
    self.height=height
    self.breadth=breadth
   def calc_cube(self):                       #function to calculate the area of a cube
    self.area=6*self.length*self.length
    self.volume=self.length**3
    print("Area of the cube:",self.area)
    print("Volume of the cube:",self.volume)
    
    self.r1=float(self.volume/self.area)
    
   def calc_sq(self):                       #function to calculate the area of square prism
     self.area=(2*self.length**2)+(4*self.height*self.length)
     self.volume=self.length*self.length*self.height
     print("Area of the square prism:",self.area)
     print("Volume of the square prism:",self.volume)
     self.r2=float(self.volume/self.area)
     
   def calc_rect(self):                     #function to calculate the area of rectangle prism
     self.area=2*((self.length*self.breadth)+(self.breadth*self.height)+(self.length*self.height))
     self.volume=self.length*self.breadth*self.height
     print("Area of the rectangular prism:",self.area)
     print("Volume of the rectangular prism:",self.volume)
     self.r3=float(self.volume/self.area)
     
   def cal_ratio(self):                    #function to calculate the ratio
     self.total=self.r1+self.r2+self.r3
     return self.total
   def show(self):
     print("Dimensions:",self.length,self.breadth,self.height,end="\n ")

n=int(input("Enter how many boxes you want to create?\n"))
B1=[] 
s1=[i for i in range(0,n)]
for i in range(0,n):
  print("\n")
  print("Enter details of box",i+1)
 
  l1=random.randint(1,1000)
  b1=random.randint(1,1000)
  h1=random.randint(1,1000)
  #B1=Box(l1,b1,h1)
  B1.append(Box(l1,b1,h1))
  print("\nCUBE:")
  B1[i].calc_cube()
  print("\nSQUARE PRISM:")
  B1[i].calc_sq()
  print("\nRECTANGULAR PRISM:")
  B1[i].calc_rect()
  s=B1[i].cal_ratio()
  print("Vol:area=",s)
  s1[i]=B1[i].total
  print("\n")
print("Details of maximum area/volume ratio:",end="\n")
max_d=s1.index(max(s1))
B1[max_d].show()