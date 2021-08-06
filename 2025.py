n = int(input())
while n:
    n -= 1
    text = input().split()
    for x in text:
        if ('oulupukk' in x):
            if len(x) == 10:
                text[text.index(x)] = 'Joulupukki'
            if len(x) == 11:
                text[text.index(x)] = 'Joulupukki.'

    text = ' '.join(text)
    print(text)