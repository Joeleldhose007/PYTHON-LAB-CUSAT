#function to input the side of the triangle
def get_side():
  side=int(input("Enter the side of the triangle:"))
  return (side)

#function to calculate area
def area():
  side_1=get_side()                      #side_1,side_2,side_3- three sides of triangle
  side_2=get_side()
  side_3=get_side()
  semi_peri=(side_1+side_2+side_3)*0.5       #semi_peri=semiperimeter of the triangle
  calculation=semi_peri*(semi_peri-side_1)*(semi_peri-side_2)*(semi_peri-side_3)
  area=calculation**0.5
  print("Area",area)
  return area

#function to calculate the contribution of each triangle
def contribution(area_1,area_2):               #area_1- area of first triangle
  print("Total",(area_1+area_2))               #area_2- area of second triangle
  con_1=(area_1/(area_1+area_2))*100           #con_1- contribution of first triangle
  con_2=(area_2/(area_1+area_2))*100           #con_2- contribution of second triangle
  print("Contribution of the first triangle",con_1)
  print("Contribution of the second triangle",con_2,"\n")

#function to be invoked
def main():
  print("\nArea of TRIANGLE")
  print("TRIANGLE 1 : ")
  area1=area()
  print("\nTRIANGLE 2 : ")
  area2=area()
  print("\nContribution of each triangle")
  contribution(area1,area2)

main()                                            #function invokation