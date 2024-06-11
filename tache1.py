dictionnaire6 = {1:"apple", 2:"banana", 3:"kiwi", 4:"cherry", 5:"watermelon", 6:"fig"}

def long_str(dictionnaire6):
    dictionnaire_filtre = {}
    for key, val in dictionnaire6.items():
        if len(val) > 5:
            dictionnaire_filtre[key] = val
    return dictionnaire_filtre

long_str(dictionnaire6)