# Write your count_char_x function here:
def count_char_x(word,x):
  i = 0
  for elt in word:
    if x == elt:
      i += 1
  return i

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
