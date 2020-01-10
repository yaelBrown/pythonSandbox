from collections import Counter

l = [1,1,1,1,1,1,1,2,2,2,22,2,2,2,2,2,3,3,3,33,3,4,4,4,4,4,5,5,5,5,5]

print(Counter(l))

s = 'asaaaasdfffffdfdsfasdfffdasdhadff'

print(Counter(s))

# How many times does each word show up in this sentence.

sentence = "this this this is a sentence where where the words words show up multiple times"
words = sentence.split()

print(Counter(words))

c = Counter(words)