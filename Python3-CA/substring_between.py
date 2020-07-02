# Write your substring_between_letters function here:
def substring_between_letters(word,start,end):
  if start in word and end in word:
    return word[word.find(start)+len(start):word.rfind(end)]
  else:
    return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
