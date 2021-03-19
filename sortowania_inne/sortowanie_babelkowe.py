#dwa sposoby na postortowanie tablicy algorytmem sortowania bąbelkowego

def bubble1(T):
    n = len(T)
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if T[i] < T[i + 1]:
                T[i], T[i + 1] = T[i + 1], T[i]
    return T

def bubble2(tab):
    for i in range(len(tab) - 1):
        for j in range(len(tab) - 1):
            if tab[j] > tab[j + 1]:
                temp = tab[j]
                tab[j] = tab[j + 1]
                tab[j + 1]= temp
    return tab    
