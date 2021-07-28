from difflib import SequenceMatcher
while True:
    try:
        word1 = input()
        word2 = input()
        x = len(word1)
        y = len(word2)
        s = SequenceMatcher(None, word1, word2)
        print(s.find_longest_match(0, x, 0, y).size)
    except EOFError:
        break

# Anather way
# def comp(word1, word2):
#     count = 0
#     i = 0
#     while i != len(word1):
#         x = ""
#         j = i
#         while j != len(word1):
#             x += word1[j]
#             if x in word2:
#                 if len(x) > count:
#                     count = len(x)
#             j += 1
#         i += 1
#     return count
# while True:
#     try:
#         word1 = input()
#         word2 = input()
#         print(comp(word1,word2))
#     except EOFError:
#         break
# Time limit exceeded