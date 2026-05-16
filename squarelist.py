nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = [0] * len(nums)
first = 0
last = len(nums) - 1

for x in range(len(nums)-1,-1,-1):
    if abs(nums[first]) > abs(nums[last]):
        temp = nums[first]
        first += 1
    else:
        temp = nums[last]
        last -= 1
    
    result[x] = temp ** 2

print(result)