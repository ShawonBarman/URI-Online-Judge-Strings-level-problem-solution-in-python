arr = []
while True:
    try:
        name = input()
        arr.append(name)
    except EOFError:
        break
arr = sorted(arr, key=lambda s: s.lower())
print(arr[len(arr)-1])