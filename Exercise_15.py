# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. 

def reverse_sentence(sentence):
   return ' '.join(sentence.split()[::-1])

sentence = input("Enter a string with mutliple words: ")
rev = reverse_sentence(sentence)
print(rev)