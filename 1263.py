from difflib import SequenceMatcher
while True:
    try:
        text = (input().lower()).split()
        total = 0
        x = False
        for i, word in enumerate(text):
            text[i] = word[0]
            if text[i] == text[i - 1] and x == False:
                x = True
                total += 1
            elif text[i] != text[i - 1]:
                x = False

        print(total)
    except EOFError:
        break