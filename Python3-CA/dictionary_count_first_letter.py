# Write your count_first_letter function here:

def count_first_letter(names):
  new_dict = {}
  for keys in names.keys():
    if keys[0] in new_dict:
      new_dict[keys[0]] += len(names[keys])
    else:
       new_dict[keys[0]] = len(names[keys])
  return new_dict

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}