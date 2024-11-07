import random
print("💫⭐️welcom to...")
print("""
╭━━━╮╱╱╱╱╱╭╮╱╱╭━━━╮
┃╭━╮┃╱╱╱╱╱┃┃╱╱┃╭━╮┃
┃╰━╯┣━━┳━━┫┃╭╮┃╰━╯┣━━┳━━┳━━┳━╮╭━━┳━━┳┳━━┳━━┳━━┳━┳━━╮
┃╭╮╭┫╭╮┃╭━┫╰╯╯┃╭━━┫╭╮┃╭╮┃┃━┫╭╯┃━━┫╭━╋┫━━┫━━┫╭╮┃╭┫━━┫
┃┃┃╰┫╰╯┃╰━┫╭╮╮┃┃╱╱┃╭╮┃╰╯┃┃━┫┃╱┣━━┃╰━┫┣━━┣━━┃╰╯┃┃┣━━┃
╰╯╰━┻━━┻━━┻╯╰╯╰╯╱╱╰╯╰┫╭━┻━━┻╯╱╰━━┻━━┻┻━━┻━━┻━━┻╯╰━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
╭━━━╮
┃╭━╮┃
┃┃╱╰╋━━┳╮╭┳━━╮
┃┃╭━┫╭╮┃╰╯┃┃━┫
┃╰┻━┃╭╮┃┃┃┃┃━┫
╰━━━┻╯╰┻┻┻┻━━╯
""")
print("⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️👾⭐️ ") 
help = input("Press (Enter) to continue or print (help) to see the rules..").lower()
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
if help == "help": 
  print(" ")
  print(" ")
  print("""                                     **********Rules**********
                           1)you will choose and the computer will choose
                           2)Rock smashes scissors -> Rock wins
                           3)scissors cut paper -> scissors win
                           4)paper covers rock -> paper wint
         """)
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
rock = ("""
█▀█ █▀█ █▀▀ █▄▀
█▀▄ █▄█ █▄▄ █░█
""")
paper = ("""
█▀█ ▄▀█ █▀█ █▀▀ █▀█
█▀▀ █▀█ █▀▀ ██▄ █▀▄
""")
scissors = ("""
█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
""")

if user_choice.lower() == "rock" and computer_choice.lower() == "rock":
  print (f"Your choice is \n {rock}")
  print (f"And the computer choice is \n {rock}")
  print ("𝕀𝕥’𝕤 𝕒 𝕥𝕚𝕖👍🏻")
elif user_choice.lower() == "paper" and computer_choice.lower() == "paper":
  print (f"Your choice is \n {paper}")
  print (f"And the computer choice is \n {paper}")
  print ("𝕀𝕥’𝕤 𝕒 𝕥𝕚𝕖👍🏻")
elif user_choice.lower() == "scissors" and computer_choice.lower() == "scissors":
  print (f"Your choice is \n {scissors}")
  print (f"And the computer choice is \n {scissors}")
  print ("𝕀𝕥’𝕤 𝕒 𝕥𝕚𝕖👍🏻")
elif user_choice.lower() == "rock" and computer_choice.lower() == "scissors":
  print (f"Your choice is \n {rock}")
  print (f"And the computer choice is \n {scissors}")
  print ("𝕐𝕠𝕦 𝕨𝕠𝕟 🎉")
elif user_choice.lower() == "rock" and computer_choice.lower() == "paper":
  print (f"Your choice is \n {rock}")
  print (f"And the computer choice is \n {paper}")
  print ("𝕐𝕠𝕦 𝕝𝕠𝕤𝕖 😔")
elif user_choice.lower() == "paper" and computer_choice.lower() == "rock":
  print(f"Your choice is \n {paper}")
  print(f"And the computer choice is \n {rock}")
  print ("𝕐𝕠𝕦 𝕨𝕠𝕟 🎉")
elif user_choice.lower() == "paper" and computer_choice.lower() == "scissors":
  print(f"Your choice is \n {paper}")
  print(f"And the computer choice is \n {scissors}")
  print ("𝕐𝕠𝕦 𝕝𝕠𝕤𝕖 😔")
elif user_choice.lower() == "scissors" and computer_choice.lower() == "rock":
  print(f"Your choice is \n {scissors}")
  print(f"And the computer choice is \n {rock}")
  print ("𝕐𝕠𝕦 𝕝𝕠𝕤𝕖 😔")
elif  user_choice.lower() == "scissors" and computer_choice.lower() == "paper":
  print(f"Your choice is \n {scissors}")
  print(f"And the computer choice is \n {paper}")
  print ("𝕐𝕠𝕦 𝕨𝕠𝕟 🎉")
else:
  print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")