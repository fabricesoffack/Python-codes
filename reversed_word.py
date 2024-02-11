
word = input("your word is: ")

#slicing method
reversed_word = word[::-1]

# join method
reversed_word = ''.join(reversed(word))

print(f"the reverse of the word {word} is: {reversed_word}")

