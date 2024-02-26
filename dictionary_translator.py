# translator english to french program

# translation_dictionary = {}

# translation_dictionary ["safou"] = " prune africaine ou poire de brousee ou Dacryodes Edulis"
# translation_dictionary ["grapefruit"] = "pamplemousse"
# translation_dictionary  ["cassimango"] = "prune de cythere"

word = input("give me a word in english: ")

translation_dictionary = {
    "safou" : " prune africaine ou poire de brousee ou Dacryodes Edulis",
    "grapefruit" : "pamplemousse",
    "cassimango" : "prune de cythere"
}

translated_word = translation_dictionary.get(word)

if translated_word:
    print(translated_word)
else:
    print(f"{word} is not in my memory")


