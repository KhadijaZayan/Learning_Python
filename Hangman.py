import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words = ["apple", "banana", "cherry", "orange", "lemone", "grape", "pineapple", "strawberry", "blueberry", "watermelon"]
random_word = random.choice(words)

display = ["_"] * len(random_word)
print(" ".join(display))

lose = 6

guessed_letters = []

while "_" in display and lose > 0:
  gussed = input("please guess a letter: ").lower()

  if gussed in guessed_letters:
    print("you already guessed this letter\n")

  if gussed not in random_word:
    lose -= 1 
    print(HANGMANPICS[6 - lose])
  else:
    for position in range(len(random_word)):
      if random_word[position] == gussed:
        display[position] = gussed
  print(" ".join(display))
  print(f"\nyou have {lose} more tries\n")
if lose == 0:
  print("""
         **********
          YOU LOSE
         **********
         """)
  print(HANGMANPICS[-1])
else:
  print("""
         *********
          YOU WIN
         *********
         """)