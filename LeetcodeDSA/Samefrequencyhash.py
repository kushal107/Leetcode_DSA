from collections import defaultdict

s = "abacbc"

counts = defaultdict(int)
for x in s:
    counts[x] += 1

ans = counts[s[0]]

for k,v in counts.items():
    if v != ans:
        print(False)
        exit()
    else:
        continue

print(True)

#another faster checking:
freq = counts.values()
final_answer = (len(set(freq)) == 1)
print(final_answer)
########################


