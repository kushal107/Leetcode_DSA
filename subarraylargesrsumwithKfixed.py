nums = [3,-1,4,12,-8,5,6]
k = 4
curr = 0
for i in range(k):
    curr += nums[i]

ans = curr

for i in range(k,len(nums)):
    curr = curr + nums[i] - nums[i-k]
    ans = max(ans,curr)

print(ans)