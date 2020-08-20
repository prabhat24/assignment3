# [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1] -- > 5
#    J
#    1                                    i = 9
#  -8 + 13
# = 5
# earlier  J ++
# Also maintain the max
# 0 . update i and j till ar [i] == 1
# 1 .Update counter as cout = (count + 1) % length of the arr
# 2. Find the length of rep ones =
# 	if (J - i) < 0:
# Result = (j -i) + L
# else
# J -i

neg = False


def count1(i, j, L):
    if j - i > 0:
        return j - i
    else:
        global neg
        neg = True
        return j - i + L


def calc(lst):
    i = 0
    j = 0
    length = len(lst)
    f: bool
    breaked: bool
    max = 0
    while (not neg):
        if (lst[i] == 1):
            j = i
            while (lst[j] != 0):
                # keep i same increment j
                j = (j + 1) % length
            # if lst[j]==0
            if count1(i, j, length) > max:
                max = count1(i, j, length)
            i = j
        i = i + 1
    return max


if __name__ == '__main__':
    lst = [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
    print(calc(lst))
