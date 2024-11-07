names = input("Enter the frist and the last name of your friends separtedvby a comma: ").split(", ")
names_list = []
for name in names:
  name_part = name.split()
  print(name_part)

  
  frist_name = name_part[0]
  last_name = name_part[1]
  frist = frist_name[0].upper()
  last = last_name[0].upper()
  full_name = frist + "." + last + "."
  print( full_name,"\n")

 