'''
If first letter of word is a vowel, add 'ay' at the end. If it's a consonate, remove first letter and add it at the end. Then add 'ay' at the end.
'''

def pig_latin(w):
  first_letter = w[0]

  # check if vowel
  if first_letter in 'aeiou':
    pig_word = w + 'ay'
  else:
    pig_word = w[1:] + first_letter + 'ay'

  return pig_word