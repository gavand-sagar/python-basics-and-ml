import numpy as np

# CPU - serial execution

# Element-wise Arithmetic
prices = np.array([100, 200, 300])
discounted_prices = prices * 0.9  # 10% off
print(discounted_prices) # [ 90. 180. 270.]
print("===============================\n\n\n")


# #Filtering Data (Boolean Indexing)
# scores = np.array([45, 88, 92, 30, 75])
# temp = scores >= 70
# # print(temp)
# passing_scores = scores[temp]
# print(passing_scores) # [88, 92, 75]
# print("===============================\n\n\n")


# Basic Statistical Analysis
# data = np.array([1, 5, 8, 12, 15, 22])

# print(f"Mean: {np.mean(data)}")
# print(f"Median: {np.median(data)}")
# print(f"Std Dev: {np.std(data)}")
# print("===============================\n\n\n")

# Creating Ranges (The Better range())
# Create 5 numbers evenly spaced between 0 and 100
# points = np.linspace(1, 10, 10)
# print(points) # [  0.  25.  50.  75. 100.]
# print("===============================\n\n\n")
# temp = np.ones(3)
# this will give us 3x3 matrix

# print(temp)


# #Reshaping Data
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# matrix = arr.reshape(3, 3)  # 2 rows, 3 columns
# print(matrix)
# print("===============================\n\n\n")


# #Generating Random Data
# Generate 5 random floats between 0 and 1
# random_nums = np.random.rand(5)
# print(random_nums * 100)
# Generate 3 random integers between 1 and 10
# random_ints = np.random.randint(1, 11, 3)
# print(random_nums)
# print(random_ints)
# print("===============================\n\n\n")


# #Finding Outliers (Argmax/Argmin)
# temperatures = np.array([22, 25, 19, 32, 21])
# hottest_day_index = np.argmax(temperatures)
# print(f"Day {hottest_day_index + 1} was the hottest.") # Day 3
# print("===============================\n\n\n")


# #Handling Missing Values
# data = np.array([1, 2, np.nan, 4])
# print(data)        # [False, False,  True, False]
# # med = np.mean(data)
# # print(med)
# clean_data = np.nan_to_num(data,nan=8) # Replace NaN with 0
# print(clean_data)  # Replace NaN with 0
# print("===============================\n\n\n")


#Stacking and Combining Arrays
# a = np.array([1, 2])
# b = np.array([3, 4])

# vertical = np.vstack((a, b))   # Stack on top
# horizontal = np.hstack((a, b)) # Side by side
# # print(vertical)
# print(horizontal)
# print(horizontal + 5)
# print((horizontal + 5) / 6)
# print("===============================\n\n\n")
