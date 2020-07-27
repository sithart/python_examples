# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  my_dictionary = {}
  for data in words:
    if data in my_dictionary:
      my_dictionary[data] += 1
    else:
      my_dictionary[data] = 1

  return my_dictionary
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}