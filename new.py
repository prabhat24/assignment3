# Abbbccccaacc
# i  -> a
# J -> b
# After printing or discarding make i = j
# And then again do the same thing till end of the loop

def check_if_print(i, j, k):
    if (j - i) < k:
        return True
    return False



def print_s(a, k):
    i = 0
    j = 0
    result = ""
    while (i <= len(a) - 1 and j <= len(a) - 1):
        while (j <= len(a) - 1 and a[i] == a[j]):
            j = j + 1
            # ari != arj
        if check_if_print(i, j, k):
            result = result + a[i:j]
        ## make i and j same
        i = j
    return result

if __name__ == '__main__':
    print(print_s("addddhhhccccmmmdddd", 4))
