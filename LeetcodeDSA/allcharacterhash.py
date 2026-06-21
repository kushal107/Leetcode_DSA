sentence = "thequickbrownfoxjumpsoverthelazdogy"
#simple solution
seen = set(sentence)
print(len(seen)== 26)

#My solution
flag = True
myset = set()
for x in sentence:
    myset.add(x)
    if ord(x) < 97 or ord(x) > 122:
        flag = False
        break
        
if len(myset) == 26 and flag == True:
    print('Yes')
else:
    print('No')

#both solutions are time complexity O(n)