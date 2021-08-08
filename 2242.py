word = input()
comp = ''
vowel = "aeiou"
for i in range(len(word)):
    if word[i] in vowel:
        comp += word[i]
rev_comp = comp[::-1]
if(comp == rev_comp):
    print('S')
else:
    print('N')