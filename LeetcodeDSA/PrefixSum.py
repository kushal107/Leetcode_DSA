nums = [2,3,5,-5,-1]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

prefix = [nums[0]]
for i in range(1,len(nums)):
    prefix.append(nums[i] + prefix[-1])

print(prefix)