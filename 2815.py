words = input().split()

for i in range(len(words)):
    if words[i][:2] == words[i][2:4]:
        words[i] = words[i][2:]

for i in range(len(words)-1):
    print(words[i],end=" ")
print(words[len(words)-1])