import random

my_list = ['a', 'b', 'a', 'd', 'a', 'f', 'a']
k = 4 # Number of random samples to select

# Get random sample with index
random_sample_with_index = random.sample(list(enumerate(my_list)), k)

# Print the result
print(random_sample_with_index)

# Separate indices and values
indices, values = zip(*random_sample_with_index)

# Print indices
print(f"Indices: {list(indices)}")

# Print values
print(f"Values: {list(values)}")