sentence = input("Please enter a sentence: ")
word = sentence.split()
words = word[: : -1]
print(" ".join(words))