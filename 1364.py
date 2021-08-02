while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    emotions = []
    for i in range(n):
        em = input()
        emotions.append(em)
    count = 0
    for i in range(m):
        text = input()
        for j in range(len(emotions)):
            if emotions[j] in text:
                count += text.count(emotions[j])
                text = text.replace(emotions[j], "")
    print(count)

# Wrong answer (15%)