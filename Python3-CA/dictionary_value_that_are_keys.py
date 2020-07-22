# Write your values_that_are_keys function here:

def values_that_are_keys(my_dictionary):
  my_list = []
  check_list = list(my_dictionary.values())
  print(check_list)
  for items in my_dictionary:
    if items in check_list:
      my_list.append(items)
  return my_list
    

    

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]