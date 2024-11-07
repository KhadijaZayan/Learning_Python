colors = []
first_color = input ("Add the frist color you like: ")
yes_no = input ("do you want to add more colors? (y/n): ")
if yes_no == "y":
  secound_color = input ("Add the secound color you like: ")
  print("the colors you like are:")
  print([first_color + " and " + secound_color])
else:
  input("ress Enter to skip...")
  print("the colors you like are:")
  print([first_color])
  
  
  
  