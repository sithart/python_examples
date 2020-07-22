# Write your add_ten function here:

def add_ten(my_dictionary):
  new_dict = {}
  for items in my_dictionary:
    new_dict[items] = ( my_dictionary[items] + 10 )
  return new_dict
    


# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}