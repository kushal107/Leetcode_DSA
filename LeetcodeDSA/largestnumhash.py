nums = [0,1]        
nums.sort()
largest_number = nums[-1]
myset = set(nums)
     
for curr_num in range(largest_number + 1):
    if curr_num not in myset:
      print(curr_num)
        
print(largest_number + 1)