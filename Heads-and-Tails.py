import random 

print("welcome to the Coin Guessing Game!")

print("Choose a methood to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")

choice = input("Enter your choice (1 or 2):")

random_number = random.random()


if choice == "1":
   random_number = random.random()
   if random_number >= 0.5:
    computer_result = "Heads"
   else:
    computer_result = "Tails"
elif choice == "2":
   if random.randint(0,1) == 0:
    computer_result = "heads"
   else:
    computer_result = "Tails"
else:
 print("Invald choice. Please enter 1 or 2.")
user_choice = input("Enter your guess (Heads) or (Tails):")
if user_choice.lower() == computer_result.lower():
  print("congratulations! you win!")
else:
  print(f"Sorry you lose the computer choice was: {computer_result}")
