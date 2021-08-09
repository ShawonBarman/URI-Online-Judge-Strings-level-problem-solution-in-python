while True:
    try:
        word = input()
        rev_word = word[len(word)-1::-1]
        x = rev_word[0]
        ans = x
        for i in range(1, len(rev_word)):
            if rev_word[i] == x:
                break
            else:
                ans += rev_word[i]
        if len(ans) == len(rev_word):
            print(rev_word[::-1])
        else:
            result = rev_word[len(ans):]
            print(result[::-1])

    except EOFError:
        break

# Wrong answer (5%)