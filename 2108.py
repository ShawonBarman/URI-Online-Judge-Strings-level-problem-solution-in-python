list_text = []
list_ans = []
maxi = -999999
big_word = ""
while True:
    text = input()
    list_text.append(text)
    if text == "0":
        break
    text = text.split()
    if len(text) == 1:
        if len(text[0]) >= maxi:
            maxi = len(text[0])
            big_word = text[0]
        list_ans.append(str(len(text[0])))
    else:
        ans = ""
        for i in range(len(text)):
            if len(text[i]) >= maxi:
                maxi = len(text[i])
                big_word = text[i]
            ans += str(len(text[i])) + "-"
        list_ans.append(ans.rstrip("-"))

for i in list_ans:
    print(i)
print("\nThe biggest word:",big_word)