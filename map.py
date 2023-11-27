from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return "".join(anagram)

words = ["beetroot", "carrots", "potatoes"]
anagrams = []

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

print([jumble(word) for word in words])

m = list(map(jumble, words))
print(m)