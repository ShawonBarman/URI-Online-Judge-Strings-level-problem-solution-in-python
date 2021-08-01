n = int(input())
arr = []
for i in range(n):
    word = input()
    arr.append(word)
l = len(arr)
total = 0
flag = 0
i = 0
x = ""
sun = False
while len(arr) != 2 and sun != True:
    x += arr[0][i]
    for w in arr:
        if x in w:
            if len(w) == 1:
                total += 1
                arr.remove(w)
                sun = True
            continue
        elif x not in w and i > 0:
            flag = 1
        elif x not in w and i == 0:
            total += 1
            arr.remove(w)
        if x not in w and flag  == 1:
            total += 2
            arr.remove(w)
            flag = 0
    i += 1
for w in arr:
    total += (len(w)-len(x))+1
print(total)
avg = total/l
print("{:.2f}".format(avg))

#wrong answer