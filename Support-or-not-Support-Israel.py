print ("⭐️⭐️  Welcome to 'support or not support Israel' game!!!!  ⭐️⭐️")
print(" ")
print(" ")
lest = ["Mc donald's", "Shiny", "Lay's", "Berger King", "Fanta", "Pizza and Berger", "Panda"] 
print (lest)
support_israel = ["Mc donald's", "Lay's", "Berger King", "Fanta"]
not_support_israel = ["Shiri", "Pizza and Berger", "Panda", "Abu Auf"]
print(" ")
print("Now you will choose a produc from the list.")
choice = input("What is your choice??? ")
#التأكد اذا كان المنج جيداً ام لا
if choice.lower() == "shiny" or choice.lower() == "pizza and berger" or choice.lower() == "panda":
  print("good choich🤩 this produc is ⭐️(( not support israel ))⭐️")

elif choice.lower() == "mc donald's" or choice.lower() == "lay's" or choice.lower() == "berger king" or choice.lower() == "fanta":
  print("Bad choice☹️ this produc is 👎🏻(( support israel ))👎🏻")

else:
  print(" ")
  print("Make sure about the spell in the nxet time, please")