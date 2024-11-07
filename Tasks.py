done_tasks = []
ongoing_tasks = []
tasks_list = input("Enter your tasks for today separated a comma:\n ").split(", ")
for task in tasks_list:
  print(f"\n{task}\n")
  visited = input(f"Did you finish {task} alredy? (yes/no): /n ").lower()
  if visited == "yes" or visited == "y":
    print("Nice jod✌️⭐️ \n")
    done_tasks.append(task)
  else:
    print("Try not to put it off😕 \n")
    ongoing_tasks.append(task)
print("------")
choice = input("Do you want to see your today's progress? (yes/no): \n").lower()
if choice == "yes" or choice == "y":
   print(f"""     ******** Done Tasks ********
   
    {done_tasks}

                ******** Ongoing Tasks ********

    {ongoing_tasks}
    """)
else:
   print("Okay...see you later😉👋🏻")