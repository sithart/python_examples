single_digits = []
for i in range(10):
  single_digits.append(i)

print(single_digits)
squares = []
for digits in single_digits:
  squares.append(digits **2)
  print(digits)
print(squares)

cubes = [data**3 for data in single_digits]

print(cubes)
