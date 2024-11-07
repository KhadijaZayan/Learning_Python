print("Welcome to the password Generator!🥇")
import random
import string

lenghth = int(input("Enter the lenghth of the password: "))
num_letters = int(input("Enter the number of letters in the password: "))
num_numbers = int(input("Enter the number of numbers in the password: "))
num_symbols = int(input("Enter the number of symbols in the password: "))


if lenghth != (num_letters + num_numbers + num_symbols):
  print("Invalide input. The sum of letters, numbers, and symbols doesn't match the password lenghty.")
else:
  letters = string.ascii_letters
  numbers = string.digits
  symbols = string.punctuation

  password_chat = (
       random.choices(letters, k = num_letters) +
       random.choices(numbers, k = num_numbers) +
       random.choices(symbols, k = num_symbols) 
  )

  random.shuffle(password_chat)
  password = "".join(password_chat)
  print(f"Your password is:\n ****   {password}    ****")