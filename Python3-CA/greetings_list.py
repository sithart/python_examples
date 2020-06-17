#Write your function here
def add_greetings(names):
  greetings_list = []
  for name in names:
    greetings_list.append("Hello, "+name)
  return greetings_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
