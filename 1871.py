while True:
    c, m = map(int, input().split())
    if c == m == 0:
        break
    ans = c + m
    ans = str(ans)
    ans = ans.replace("0", "")
    print(int(ans))