flag = 0
while True:
    n = int(input())
    if n == 0:
        break
    if flag == 1:
        print("")
    arr = []
    maxi = -99999
    for i in range(n):
        word = input().upper()
        arr.append(word)
        if len(word) > maxi:
            maxi = len(word)
    for i in arr:
        diff = maxi - len(i)
        for j in range(diff):
            print(" ",end="")
        print(i)
    flag = 1

# 30% presenta0tion error