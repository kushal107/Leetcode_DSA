s = 'AABBCDDEF'
'''
myhash = {}
i = 0
for x in s:
    myhash[x] = i
    i = i+1

print(myhash)

for current_index, x in enumerate(s):
    if current_index != myhash[x]:
        print(x)
        exit()
'''

#SET solution:

seen = set()
for x in s:
    if x in seen:
        print(x)
        exit()
    else:
        seen.add(x)