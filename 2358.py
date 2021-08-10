n = int(input())
s = []
while n != 0:
    n -= 1
    name = input()
    s.append(name)
r = input()
for i in range(len(s)):
    if r in s[i]:
        while r in s[i]:
            s[i] = s[i].replace(r, "")

max_seq = ""
for i in range(len(s[0])):
    ans = ""
    for j in range(i, len(s[0])):
        ans += s[0][j]
        for k in range(1, len(s)):
            if ans in s[k]:
                if len(ans) > len(max_seq):
                    max_seq = ans
print(max_seq)