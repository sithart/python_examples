#Write your function here
def exponents(bases,powers):
  new_lst = []
  for a in bases:
    for b in powers:
      new_lst.append(a**b)

  return new_lst
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
