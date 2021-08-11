n = int(input())
while n != 0:
    n -= 1
    word1 = input()
    word2 = input()
    word3 = input()
    possibility = 0
    ans = ""
    for i in range(len(word3)):
        if word3[i] == '_':
            if possibility == 0:
                ans += word1[i]
                ans += word2[i]
            else:
                ans += word1[i]
                ans += word2[i]
            possibility += 1
    if ans[0] == ans[2] or ans[0] == ans[3]:
        print("Y")
    elif ans[1] == ans[2] or ans[1] == ans[3]:
        print("Y")
    else:
        print("N")