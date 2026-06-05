nums = [3,3]
target = 6

my_dict = {}
for index,x in enumerate(nums):
    temp = target-x
    my_dict[temp] = index

flag = False
for i,x in enumerate(nums):
    if x in my_dict.keys() and i != my_dict[x]:
        flag = True
        break

if flag == True :
    print(i,my_dict[x])
else:
    print('No')
