while True:
    n = int(input())
    if n == 0:
        break
    arr = [0] * 26
    another_arr = [0] * 26
    s = 0
    p = 0
    for i in range(n):
        x, t, y = input().split()
        position = ord(x) - 65
        if y == "correct":
            s += 1
            p += int(t)
            arr[position] = 1
        if y == "incorrect":
            another_arr[position] += 20
    for posi in range(len(arr)):
        if arr[posi]:
            p += another_arr[posi]
    print(s,p)