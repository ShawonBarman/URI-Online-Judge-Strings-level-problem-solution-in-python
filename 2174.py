n = int(input())
arr = []
while n != 0:
    n -= 1
    name = input()
    if name not in arr:
        arr.append(name)
print("Falta(m) {} pomekon(s).".format(151-len(arr)))