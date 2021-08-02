n = int(input())
while n != 0:
    n -= 1
    word = input().lower()
    if len(word) == 3:
        one = 0
        two = 0
        x = 'one'
        y = 'two'
        for j in range(len(word)):
            if word[j] == x[j]:
                one += 1
            elif word[j] == y[j]:
                two += 1
        if one >= 2:
            print(1)
        if two >= 2:
            print(2)
    if len(word) == 5:
        three = 0
        for j in range(len(word)):
            if word[j] in "three":
                three += 1
        if three >= 4:
            print(3)