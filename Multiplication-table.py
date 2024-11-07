print ("Welcom to the '⭐ ️Multiplication table ⭐️'\n ")
numder = input ("Please enter a numder: ")
print (f"The multipication table to {numder}:  \n")
for i in range (1,11):
  result = i * int(numder)
  print (f"{numder} x {i} = {result}")
