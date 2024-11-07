import random
computer_choice = random.randint(1,10)
guess = int(input("Guess a number between 1 to 10: "))
while guess != computer_choice:
  if guess > computer_choice:
    print("Too high")
  else:("Too low")
  guess = int(input("Guess a number between 1 to 10: "))
print("Your guess is correct")