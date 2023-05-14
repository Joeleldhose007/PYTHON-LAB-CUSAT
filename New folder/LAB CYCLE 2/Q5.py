class threeDshapes:
    #defining function
    def printArea(self):
        print("AREA:",self._area)
    def printVol(self):
        print("VOLUME:",self._volume)
        #Inheriting threeDshapes to cylinder
class Cylinder(threeDshapes):
    # defining function
    def __init__(self,radius,height):
        self.__radius=radius
        self.__height=height
    def area(self):
       self._area =2*3.14*self.__radius*(self.__radius+self.__height)
    def volume(self):
       self._volume =3.14*(self.__radius*self.__radius)*self.__height
# Inheriting  threeDshapes to sphere
class Sphere(threeDshapes):
    def __init__(self,radius):
       self.__r = radius
    def area(self):
       self._area = 4*3.14*self.__r*self.__r
    def volume(self):
       self._volume = (4/3)*3.14*(self.__r**3)

#object of class cylinder
cy_radius = int(input("Enter the radius of the cylinder "))
cy_height = int(input("Enter the height of the cylinder "))
c1=Cylinder(cy_radius,cy_height)
c1.area()
c1.printArea()
c1.volume()
c1.printVol()

#object of class sphere
sp_radius = int(input("\nEnter the radius of the sphere "))
s1=Sphere(sp_radius)
s1.area()
s1.volume()
s1.printArea()
s1.printVol()