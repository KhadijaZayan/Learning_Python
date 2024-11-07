#الطريقة الاولة
import random
print("Welcome to 'whose wallet?'game..\nyou will give me a list of names, and I will pick a person to pay.")
names = input ("If you ready, enter the names separated by a comma: ").split(", ")
random_choice = random.choice(names)
print(f"Please ask '{random_choice}' to take his/her wallet out. Dinner is on him/her.")
print("\n\n")
#الطريقة الثانية
import random
print("Welcome to 'whose wallet?' game...")
print("You will give a list of names, and I will pick person to pay.")
names_string = input("If you're ready, enter the names separating a comma: ")
names = names_string.split(", ")
length = len("names") - 1
random_number = random.randint(0,length)
random_person = names[random_number]
print(f"Please ask '{random_person}' to ake his/her wallet out. Dinner is on him/her")