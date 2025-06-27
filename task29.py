sonlar = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]
noyob = []

for son in sonlar:
    if sonlar.count(son) == 1:
        noyob.append(son)

print(noyob)
