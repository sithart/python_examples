#Write your function here
def larger_sum(lst1,lst2):
  i = 0
  j = 0
  for a in lst1:
    i += a
  for b in lst2:
    j += b
  print(i,j)
  if i == j:
    return lst1
  elif i > j:
    return lst1
  elif j > i:
    return lst2


#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
