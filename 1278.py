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
        word = (input().upper()).split()
        text = word[0]
        for j in range(1,len(word)):
            text = text + " " + word[j]
        arr.append(text)
        if len(text) > maxi:
            maxi = len(text)
    print(maxi)
    print(arr)
    for i in arr:
        diff = maxi - len(i)
        for j in range(diff):
            print(" ",end="")
        print(i)
    flag = 1

# 30% presenta0tion error