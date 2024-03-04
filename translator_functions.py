# function

def translated_word(word):
    if word in dictionary: 
        return f"the word translated in english is {translation}"
    else:
        return f"{word} is not in my memory"

# Main program

word = input("give me a word in english:")

dictionary = {
    "safou" : "prune africaine ou poire de brousee ou Dacryodes Edulis",
    "grapefruit" : "pamplemousse",
    "cassimango" : "prune de cythere"
}

translation = dictionary.get(word)

print(translated_word(word))

