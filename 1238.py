n = int(input())
while n != 0:
    n -= 1
    s1, s2 = map(str, input().split())
    ans = ""
    i = 0
    j = 0
    while len(ans) != (len(s1)+len(s2)):
        if i < len(s1):
            ans += s1[i]
        if j < len(s2):
            ans += s2[j]
        i += 1
        j += 1
    print(ans)