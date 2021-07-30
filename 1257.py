import string
alphabet_list = list(string.ascii_uppercase)
n = int(input())
while n != 0:
    n -= 1
    l = int(input())
    sum = 0
    for i in range(l):
        text = input().upper()
        for j in range(len(text)):
            pos = alphabet_list.index(text[j])
            sum += (pos + j + i)
    print(sum)