#Write your function here
def max_num(nums):
  if len(nums) > 1:
    for elt in nums:
      if elt > nums[0]:
        return elt
  elif len(nums) == 1:
    return nums[0]


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))


# a =  [95, 39, 76, 84, 19, 97, 26, 34]
# while len(a) > 1:
#     a = [x for x in a if x > a[0]]
# print (a)    # [97]   
