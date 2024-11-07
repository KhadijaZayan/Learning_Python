names = input("Enter the names of attendees by commas: ")
names_list = names.split(", ")
for name in names_list:
  print(f"\n{name}\n")
  attendance = input("Is this person attending? (y/n): ")
  if attendance.lower() == "y" or attendance.lower() == "yes":
    print("Attendance confirmed!")
    print("_________")
  else:
    print("Attendace not confirmed!")
    print("_________")