nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

prefix = [0]*1
prefix[0] = nums[0]
for i in range(1,len(nums)):
    prefix.append(nums[i] + prefix[-1])

print(prefix)