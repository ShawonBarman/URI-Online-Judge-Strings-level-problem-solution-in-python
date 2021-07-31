n = int(input())
while n != 0:
    n -= 1
    text = input().lower()
    t = text.replace(".", " ")
    x = t.split()
    ans = ""
    if len(x) != 0:
        for i in x:
            ans += i[0]
    print(ans)