n = int(input())
while n != 0:
    n -= 1
    message = input().upper()
    number = int(input())
    ans = ""
    for i in range(len(message)):
        if (ord(message[i]) - number) < 65:
            ans += chr((ord(message[i]) - number) + 26)
        else:
            ans += chr(ord(message[i]) - number)
    print(ans)