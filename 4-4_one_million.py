# Make a list of numbers 1-1,000,000 and print
nums = []
for i in range(1, 1000001):
    nums.append(i)
    print(nums[i-1])
