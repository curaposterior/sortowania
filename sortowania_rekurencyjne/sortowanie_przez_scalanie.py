def merge(T, lewy, prawy, pivot):
    pom = [0] * len(T) #stworzenie odpowiedniej listy pomocniczej
    for i in range(lewy, prawy + 1):
        pom[i] = T[i]
    
    i_lewy = lewy
    i_prawy = pivot + 1
    index = lewy

    while i_lewy <= pivot and i_prawy <= prawy:
        if pom[i_lewy] <= pom[i_prawy]:
            T[index] = pom[i_lewy]
            i_lewy += 1
        else:
            T[index] = pom[i_prawy]
            i_prawy += 1
        index += 1
    
    while i_lewy <= pivot:
        T[index] = pom[i_lewy]
        index += 1
        i_lewy += 1

def mergesort(T, lewy, prawy):
    if lewy != prawy:
        pivot = (lewy + prawy) // 2
        mergesort(T, lewy, pivot)
        mergesort(T, pivot + 1, prawy)
        merge(T, lewy, prawy, pivot)
    return T
