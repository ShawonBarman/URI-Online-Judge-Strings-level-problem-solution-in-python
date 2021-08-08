c = int(input())
while c != 0:
    c -= 1
    e, b = map(int, input().split())
    first = ""
    second = ""
    for i in range(e, b+1):
        first += str(i)
    second = first[::-1]
    print(first + second)