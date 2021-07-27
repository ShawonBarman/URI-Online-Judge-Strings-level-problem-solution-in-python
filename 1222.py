import math
while True:
    try:
        n, l, c = map(int, input().split())
        story = input()
        if len(story.split()) == n:
            count = 0
            x = 0
            y = 0
            for i in range(len(story)):
                if y <= c:
                    y += 1
                if y >= c:
                    y = 0
                    x += 1
            if y > 0 and y <= 20:
                x += 1
            print(math.ceil(x/l))

    except EOFError:
        break

#15% wrong solution