import torch

# GPU - parallel

# Element-wise Arithmetic
prices = torch.tensor([100, 200, 300])
discounted_prices = prices * 0.9  # 10% off
print(discounted_prices) # tensor([ 90., 180., 270.])
print("===============================\n")

# # Filtering Data (Boolean Indexing)
scores = torch.tensor([45, 88, 92, 30, 75])
passing_scores = scores[scores >= 70]
print(passing_scores) # tensor([88, 92, 75])
print("===============================\n")

# # Basic Statistical Analysis
# # Note: PyTorch stats usually require float types
data = torch.tensor([1, 5, 8, 12, 15, 22], dtype=torch.float32)

print(f"Mean: {torch.mean(data)}")
print(f"Median: {torch.median(data)}")
print(f"Std Dev: {torch.std(data)}")
# print("===============================\n")

# # Creating Ranges
points = torch.linspace(0, 100, 4)
print(points) # tensor([  0.,  25.,  50.,  75., 100.])
# print("===============================\n")

# # Reshaping Data
arr = torch.tensor([1, 2, 3, 4, 5, 6])
# PyTorch uses .view() or .reshape()
matrix = arr.reshape(2, 3) 
print(matrix)
# print("===============================\n")

# # Generating Random Data
# # 5 random floats between 0 and 1
random_nums = torch.rand(5)

# # 3 random integers between 1 (inclusive) and 11 (exclusive)
random_ints = torch.randint(1, 11, (3,))
print(random_nums)
print(random_ints)
print("===============================\n")

# # Finding Outliers (Argmax/Argmin)
temperatures = torch.tensor([22, 25, 19, 32, 21])
hottest_day_index = torch.argmax(temperatures)
print(f"Day {hottest_day_index} was the hottest.") # Day 3
print("===============================\n")

# # Handling Missing Values
# data = torch.tensor([1, 2, float('nan'), 4])
# print(torch.isnan(data))        # tensor([False, False,  True, False])
# clean_data = torch.nan_to_num(data, nan=0.0) # Replace NaN with 0
# print(clean_data)
# print("===============================\n")

# # Stacking and Combining Arrays
# a = torch.tensor([1, 2])
# b = torch.tensor([3, 4])

# # vstack and hstack work, but torch.stack or torch.cat are also common
# vertical = torch.vstack((a, b))   
# horizontal = torch.hstack((a, b)) 
# print(vertical)
# print(horizontal)
# print("===============================\n")