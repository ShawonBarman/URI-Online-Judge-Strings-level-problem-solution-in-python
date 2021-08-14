c = int(input())
while c != 0:
    c -= 1
    message = input()
    message = message[::-1]
    ans = ""
    for x in message:
        if x.islower():
            ans += x
    print(ans)