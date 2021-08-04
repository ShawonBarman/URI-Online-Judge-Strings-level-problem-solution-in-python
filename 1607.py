n = int(input())
while n != 0:
    n -= 1
    word1, word2 = input().split()
    sum = 0
    for i in range(len(word1)):
        ax = ord(word2[i]) - ord(word1[i])
        if ax < 0:
            sum += ax + 26
        else:
            sum += ax
    print(sum)