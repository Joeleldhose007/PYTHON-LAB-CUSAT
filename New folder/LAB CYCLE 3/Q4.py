import pickle


class vehicle:
  def __init__(self):
    self.eno=int(input("Engine number:"))
    self.model=input("Model :")
    self.typ=input("Type: ")
    self.mil=input("Mileage:")
    self.vend=input("Vendor:")
    self.reg_no=int(input("Registration number:"))
    self.oname=input("Owner name:")
  def show(self):
    sh={"Engine number":self.eno,"Model":self.model,"Type":self.typ,"Mileage":self.mil,"Vendor":self.vend,"Registration number":self.reg_no,"Owner ":self.oname}
    return sh
class sev_vehicles:
    def __init__(self,n):
      self.show_det=[]
      for i in range(0,n):
        print("Details of vehicle ",i+1)
        sh=vehicle()
        self.show_det.append(sh.show())
    def show(self):
        self.show_det=sorted(self.show_det,key=lambda d:d['Mileage'])
        print()
        return self.show_det
    def add_new(self):
     V=vehicle()
     self.show_det.append(V.show())
    def remove_veh(self,reg_no):
     f=0
     for i in self.show_det:
       if i['Registration number']==reg_no:
         self.show_det.remove(i)
         f=1
         break
     if f==0:
      print("No vehicle found!!")
    def modify(self,reg_no):
        f=0
        for i in self.show_det:
          if i['Registration number']==reg_no:
            f=1
            print(i)
            print(" ")
            print("\n1.Engine number \n2.Model \n3.Type \n4.Mileage\n")
            print("5.Vendor\n 6.Owner\n")
            choice=int(input("Enter the item to be changed\n"))
            if choice==1:
              e=int(input("Engine number\n:"))
              i['Engine number']=e
            elif choice==2:
              e=input("New model\n")
              i['Model']=e
            elif choice==3:
              e=input("New type\n")
              i['Type']==e
            elif choice==4:
              e=input("New Mileage\n")
              i['Mileage']==e
            elif choice==5:
              e=input("New Vendor\n")
              i['Vendor']==e
            elif choice==6:
              e=input("New Owner:\n")
              i['Owner']==e
            else:
              print("Invalid!!")
              f=1
              break
        if f==0:
          print("Vehicle not found!!")
n=int(input("Enter how many vehicles to enter\n"))
S=sev_vehicles(n)
f=True
while f:
  print("\n1.Show the collection\n2.Add a new vehicle\n3.Remove a vehicle\n4.Modify\n")
  print("5.Exit\n")
  choice=int(input("Enter a choice from the menu:\n"))
  if choice==1:
    V1=S.show()
    for i in V1:
      print(i)
  elif choice==2:
    S.add_new()
  elif choice==3:
    n1=int(input("Enter registration no:\n"))
    S.remove_veh(n1)
  elif choice==4:
    n1=int(input("Enter registration number:\n"))
    S.modify(n1)
  elif choice==5:
    f=False
  else:
      print("Invalid input!!\n")
S1=S.show()
print("Sorted collection acc to mileage")
print(S1)
print("\n")

file=open("file.pkl",'wb')
pickle.dump(S1,file)
file.close()
file=open("file.pkl",'rb')
S1=pickle.load(file)