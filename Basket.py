desert = [["Apples", "bananas",] , ["Milk", "Water"]]
print(desert)
input("Press enter to change the content .....")
desert[0].insert(0,"Oranges")
desert[0].insert(3,"Kiwis")
desert[1].insert(4,"Coffee")
desert[1].remove("Water")
desert[1].insert(5,"Tea")
desert.append([1, 2, 3])
print(" Here is the updated")
print(desert)
question_1 = input("Do you want to add 'strawberry'?")
if question_1.lower() == "yes":
  desert[0].insert(4,"Strawderry")
  print("success..")
  print(f"The list now is: {desert}\nGooddey now")
else:
  question_2 = input("Ok..Do yo want to add 'juice'?")
  if question_2.lower() == "yes":
    desert[1].insert(6,"Juice")
    print("success")
    print(f"Now the list now is: {desert}\nGoodbey now")
  else:
    print ("That is fine..goodbey now")
    
