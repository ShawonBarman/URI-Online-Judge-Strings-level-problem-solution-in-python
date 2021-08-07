n = int(input())
text = list(map(str, input().split()))[:n]
ans = ""
for word in text:
    if word.startswith("OB") and len(word) == 3:
        ans += "OBI" + " "
    elif word.startswith("UR") and len(word) == 3:
        ans += "URI" + " "
    else:
        ans += word + " "

print(ans.strip())