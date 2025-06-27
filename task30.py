sozlar = ["alla", "kok", "salom", "non", "kitob"]
palindromlar = []

for soz in sozlar:
    if soz == soz[::-1]:
        palindromlar.append(soz)

print(palindromlar)
