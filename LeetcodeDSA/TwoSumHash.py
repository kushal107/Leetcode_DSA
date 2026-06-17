mylist = [5,8,8,1,111]
target = 16
myhash = {}
i = 0

#create a complement hashmap where complement are keys and index is value
for x in mylist:
    myhash[target-x] = i
    i += 1

found = False

for current_index, x in enumerate(mylist):
    if x in myhash and myhash[x] != current_index:
        found = True
        print(current_index, myhash[x])
        exit()

if found == False:
    print('Not Present')


