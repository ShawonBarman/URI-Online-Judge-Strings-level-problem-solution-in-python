import re
n = int(input())
while n > 0:
    n -= 1
    c = input()
    c = re.sub('a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|x|y|z|w', ' ', c.lower()).split()
    sum = int(c[0]) + int(c[1]) + int(c[2])
    print(sum)