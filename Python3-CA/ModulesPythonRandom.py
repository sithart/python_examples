# Import random below:
import random

# Create random_list below:

random_list = []
# Create randomer_number below:
random_list = [random.randint(1,100+1) for i in range(101)]
print(random_list)
# Print randomer_number below:

randomer_number = random.choice(random_list)

print(randomer_number)
