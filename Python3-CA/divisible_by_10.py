#Write your function here
def divisible_by_ten(nums):
  i = 0
  for elt in nums:
    if elt % 10 == 0:
      i += 1
  return i



#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
