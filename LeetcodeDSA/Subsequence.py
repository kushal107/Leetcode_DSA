s = input('Enter the sequence: ')
t = input('Enter the true string: ')

s1 = t1 = 0
flag = False

if s == t:
    flag = True

len_s = len(s)
len_t = len(t)

while s1 < len_s and t1 < len_t:
    if s[s1] == t[t1]:
        s1 += 1
        t1 += 1
    else:
        t1 += 1

if s1 == len_s:
    flag = True

if flag:
    print('Contains sequence')
else:
    print('Does not contain sequence')

