s = input("Enter elements: ").split()
length = len(s)
first = 0
last = length - 1
temp = s[first]
while first != last and first < last:
    s[first] = s[last]
    s[last] = temp
    first += 1
    last -= 1
    temp = s[first]

print(f"\n{s}")
