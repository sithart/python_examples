# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  wr1 = word1[1:]
  wr2 = word2[1:]
  wr = word1[0]
  word1 = word2[0]+wr1
  word2 = wr+wr2
  return word1 + ' ' + word2
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
