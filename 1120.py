while True:
    d, n = input().split()
    if d == '0' and n == '0':
        break
    ans = "0"
    for i in range(len(n)):
        if d == n[i]:
            continue
        else:
            ans += n[i]
    print(int(ans))