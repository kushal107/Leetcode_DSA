list1 = [30, 35, 45, 50, 55, 65, 75]
list2 = [34, 38, 42, 46]
final_list = []

p1, p2 = 0, 0
len1 = len(list1)
len2 = len(list2)

while p1 < len1 and p2 < len2:
    if list1[p1] > list2[p2]:
        final_list.append(list2[p2])
        p2 += 1
    else:
        final_list.append(list1[p1])
        p1 += 1

while p1 < len1:
    final_list.append(list1[p1])
    p1 += 1

while p2 < len2:
    final_list.append(list2[p2])
    p2 += 1

print(final_list)