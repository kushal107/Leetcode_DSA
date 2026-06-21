from collections import defaultdict
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

counts = defaultdict(int)

for arr in nums:
    for n in arr:
        counts[n] += 1

length = len(nums)
ans = []

for k,v in counts.items():
    if v == length:
        ans.append(k)

ans.sort()
print(ans)