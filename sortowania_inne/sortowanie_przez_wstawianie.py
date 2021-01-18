def insertionsort(T):
    for granica in range(1, len(T)):
        element = T[granica]
        index = granica - 1
        while index >= 0 and T[index] > element:
            if T[index] > element:
                T[index + 1] = T[index]
                index -= 1
        T[index + 1] = element
    return T
