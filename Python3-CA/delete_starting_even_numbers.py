#Write your function here

def delete_starting_evens(lst):
  newlst = []
  for i in lst:
    if i%2==0:
      continue
    elif i%2!=0:
      newlst = lst[lst.index(i):]
      break
  return newlst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))
