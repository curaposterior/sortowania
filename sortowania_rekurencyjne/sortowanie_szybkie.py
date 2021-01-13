#sortowanie szybkie
#pivot to indeks ostatniego elementu

def wyznaczPivot(T, i_lewy, i_prawy):
    granica = i_lewy
    pivotIndex = i_prawy
    for i in range(i_lewy, i_prawy):
        if T[i] < T[pivotIndex]:
            zamiana = T[i]
            T[i] = T[granica]
            T[granica] = zamiana
            granica += 1
    
    zamianaWartosciPivota = T[granica]
    T[granica] = T[pivotIndex]
    T[pivotIndex] = zamianaWartosciPivota

    return granica

def sortowanie_szybkie(T, i_lewy, i_prawy):
    if i_lewy < i_prawy:
        pivotIndex = wyznaczPivot(T, i_lewy, i_prawy)
        sortowanie_szybkie(T, i_lewy, pivotIndex - 1)
        sortowanie_szybkie(T, pivotIndex + 1, i_prawy)
    return T