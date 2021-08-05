n = int(input())
fixed_char = "AEIOS"
while n != 0:
    n -= 1
    word = input()
    ans = 1
    for i in range(len(word)):
        flag = False
        for j in range(len(fixed_char)):
            if word[i].lower() == fixed_char[j].lower():
                flag = True
        if flag:
            ans *= 3
        else:
            ans *= 2
    print(ans)