#reversed_firstname

word = "fabrice"
length = len(word)  # This is 7 for "fabrice"
list=[]

# forward Index = i (the index of the element in the sequence starting from 0)
# reversed Index = N - i -1
# N = length(len) = the total number of elements in the sequence

for i in range(length):
    forward_index = i
    reversed_index = length-forward_index-1
    list.append(word[reversed_index])
print(list)
