def fact5(liste):
    minimum  = max(liste)
    for valeur in liste:
        if valeur < minimum:
            minimum = valeur
    return minimum

fact5([1,4,6,5])