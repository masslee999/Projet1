def fact6(liste):
    somme = 0
    for nbr in liste:
        somme += nbr
    Mean = round(somme/ 7, 2)
    return somme, Mean

fact6([1,4,6,5])