sozlar = ["AI", "hello", "assalomu", "kitob", "ha", "world", "dasturlash"]
qisqa = []
orta = []
uzun = []

for soz in sozlar:
    if len(soz) <= 3:
        qisqa.append(soz)
    elif 4 <= len(soz) <= 6:
        orta.append(soz)
    else:
        uzun.append(soz)

print("Qisqa:", qisqa)
print("O'rta:", orta)
print("Uzun:", uzun)
