n = int(input())
while n != 0:
    n -= 1
    name = input()
    mixed_name = input()
    full_name = ""
    if len(name) % 2 == 0:
        for i in range(0, len(name), 2):
            full_name += name[i:i+2]
            for j in range(i, i+1):
                full_name += mixed_name[j:j+2]

    print(full_name)