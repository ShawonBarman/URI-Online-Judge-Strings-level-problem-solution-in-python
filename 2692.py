n, m = map(int, input().split())
array1 = []
array2 = []
for i in range(n):
    e, s = input().split()
    array1.append(e)
    array2.append(s)
for i in range(m):
    text = input()
    ans = ""
    for x in text:
        if x in array1:
            for j in range(len(array1)):
                if x == array1[j]:
                    ans += array2[j]
        elif x in array2:
            for j in range(len(array2)):
                if x == array2[j]:
                    ans += array1[j]
        else:
            ans += x
    print(ans)