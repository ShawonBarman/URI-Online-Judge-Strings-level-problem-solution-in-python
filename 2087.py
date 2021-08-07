while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        word = input()
        arr.append(word)
    flag = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j].startswith(arr[i]):
                flag = 1
    if flag == 1:
        print("Conjunto Ruim")
    else:
        print("Conjunto Bom")