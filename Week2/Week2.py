# A
def reorderDigits(list, direction):
    x = []
    for i in list:
        if direction == "asc":
            x.append(int("".join(sorted(str(i)))))
        elif direction == "desc":
            x.append(int("".join(sorted(str(i), reverse=True))))
    print(x)

reorderDigits([515, 341, 98, 44, 211], "asc")
reorderDigits([515, 341, 98, 44, 211], "desc")
reorderDigits([63251, 78221], "asc")
reorderDigits([63251, 78221], "desc")
reorderDigits([1, 2, 3, 4], "asc")
reorderDigits([1, 2, 3, 4], "desc")


# B
def canPartition(list):
    for i in range(0, len(list)):
        x = list[i]
        list.pop(i)
        y = 1
        for j in list:
            y *= j
        if x == y:
            print("true")
            break
        list.insert(i, x)
    else:
        print("false")

canPartition([2,8,4,1])
canPartition([-1,-10,1,-2,20])
canPartition([-1,-20,5,-1,-2,2])







