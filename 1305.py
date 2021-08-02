while True:
    try:
        num = input()
        if "." not in num:
            print(int(num))
        else:
            ind = num.index(".")
            first = num[:ind]
            last = num[ind+1:]
            if first != "":
                first = int(first)
                if last != "":
                    if (int(last[0]) > 0 and first > 0) or (first == 0 and int(last[0]) == 5):
                        first += 1
                if first > 0:
                    print(first)
    except EOFError:
        break

#10% wrong answer

#Using c language
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#
# void main()
# {
# 	char num[100];
# 	char cutoff[100];
#
# 	while (scanf("%s %s", num, cutoff) != EOF)
# 	{
#
# 		int x = atoi(num);
# 		double frac = atof(num) - x;
# 		double _cutoff = atof(cutoff);
#
# 		if (frac > _cutoff)
# 			x++;
#
# 		printf("%d\n", x);
# 	}
# }