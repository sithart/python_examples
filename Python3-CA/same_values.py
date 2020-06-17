#Write your function here
def same_values(lst1, lst2):
  new_lst = []

  # for a in lst1:
  #   for b in lst2:
  #     if a == b:
  #         indices = lst1.index(a)
  #         if indices not in new_lst:
  #           new_lst.append(indices)
  # return new_lst

  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
