numbers = [1, 2, 3, 4, 5,]
print(numbers)
print("Let's add each number to the next..")
total = 0
for number in numbers:
  total += number
  print(f"-> {total}\n")
print(f"The total number is: {total}")
