#Write your function here
def odd_indices(lst):
  new_lst = []
  for i in range(len(lst)):
    if i % 2 == 0:
      continue
    new_lst.append(lst[i])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
