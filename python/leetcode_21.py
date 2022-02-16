def mergeTwoLists(l1,l2):
    l3 = []
    i,j = 0,0

    while (True):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        elif l2[j] < l1[i]:
            l3.append(l2[j])
            j += 1
        elif l2[j] == l1[i]:
            l3.append(l2[j])
            l3.append(l1[i])
            i += 1
            j += 1

        if i >= len(l1):
            break

        if j >= len(l2):
            break

    if i < len(l1):
        while True:
            l3.append(l1[i])
            i += 1

            if i >= len(l1):
                break

    if j < len(l2):
        while True:
            l3.append(l2[j])
            j += 1

            if j >= len(l2):
                break

    return (l3)

if __name__ == '__main__':
    l1 = [1,4,6]
    l2 = [2,3,6,7,8,9,90]
    print (mergeTwoLists(l1,l2))