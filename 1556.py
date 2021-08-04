flag = 0
while True:
    try:
        word = input()
        if flag == 1:
            print()
        word = sorted(word)
        arr = []
        for i in range(len(word)):
            ans = word[i]
            if ans not in arr:
                arr.append(ans)
            for j in range(i+1, len(word)):
                ans += word[j]
                if ans not in arr:
                    arr.append(ans)
            for j in range(i+1, len(word)):
                x = word[i]+word[j]
                if x not in arr:
                    arr.append(x)
        for i in arr:
            print(i)
        flag = 1
    except EOFError:
        break

# from itertools import permutations
# while True:
#     try:
#         word = input()
#         possiveis = [''.join(p) for p in permutations(word)]
#         print(possiveis)
#     except EOFError:
#         break