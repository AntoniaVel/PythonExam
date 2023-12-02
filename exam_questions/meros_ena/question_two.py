import random


# Ekfwnisi
def f(L):
    if len(L) == 1:
        return L[0]  # An yparxei mono ena stoixeio, tote einai to max
    m = len(L) // 2  # Messaio stoixeio tis listas
    x = f(L[:m])  # Prwto miso tis listas input stin f
    y = f(L[m:])  # Deutero miso tis listas input stin f
    if x > y:
        return x
    else:
        return y


# O algorithmos that xvrizei ti lista kai tis ypolistes sti mesi mexri na ftasei anadromika se lista 2 stoixeiwn.
# Tore sygkrinei ta stoixeia kai epistrefei to megalytero. Me auto ton tropo anadromika vriskei to max.
# px: [8, 11, 4, 18, 25]
#     [8, 11] kai [4, 18, 25]
#     x = 8, y = 11 kai [4, 18, 25]
#     return 11 kai [4] kai [18, 25]
#     return 11 kai return 4  kai x = 18, y = 25
#     return 11 kai return 4  kai return 25
# Kathe return kai kathe diaxwrismos einai mia anadromim


# Lysi:
# Ypolologizei kai epistrefei to max tis listas
def f2(L):
    return max(L)


lst = [random.randint(1, 25) for x in range(5)]
print(lst)
print(f(lst))
print(f2(lst))

# Notes:
#   // -> div (teleia diairesi)
#   lst[:5] -> ta 5 prwta stoixeia tis listas
#   lst[5:] -> ta 5 teleutaia stoixeia tis listas
