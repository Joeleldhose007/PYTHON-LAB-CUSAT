#function - to print all possible substrings
def sub_strings(name):
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      print(s, end=",")

#function - to print all possible substrings with length specified
def sub_strings_with_length(name,size):
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      if len(s)==size:
        print(s,end=" , ")

#function - to print all possible substrings with length and no of distinct characters specified
def sub_strings_with_N_characters(name,size,N):
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      if len(s)==size:
        distinct = set(s)
        if len(distinct) == N:
          print(s,end=" , ")

#function - to print all possible substrings with max length and N no of distinct characters
def sub_strings_with_max_length_with_N_characters(name,N):
  string_list = []
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      distinct = set(s)
      if len(distinct) == N:
        string_list.append(s)

  length = len(max(string_list,key = len)) 
  for i in string_list:
    if len(i)==length:
      print(i,end=" , ")

#function - to print all the paliandrome substrings
def print_paliandrome(name):
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      reverse = s[::-1]
      if reverse == s:
        print(s , end = " , ")


name = input("Enter the string ")
print("All the Possible Sub Strings are")
sub_strings(name) #prints all possible sub-strings

length = int(input("\nEnter the length of the substrings you want to print "))
#prints all possible sub-strings with length specified
print("\nAll the Possible Sub Strings with length ",length," are")
sub_strings_with_length(name,length) 

num_of_distinct = int(input("\nEnter the no of distinct characters you want to print "))
#prints all possible sub-strings with length and no of distinct characters
print("\nAll the Possible Sub Strings with length ",length,"and 
",num_of_distinct," distinct characters are")
sub_strings_with_N_characters(name,length,num_of_distinct)

#prints all sub-strings with max-length and no of distinct characters given
print("\nSub Strings with Max - Length and ",num_of_distinct," characters")
sub_strings_with_max_length_with_N_characters(name,num_of_distinct)

#prints all the paliandrome sub-strings
print("\nThe Paliandrome Strings are ")
print_paliandrome(name)