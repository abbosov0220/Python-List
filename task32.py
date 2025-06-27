sozlar = ["kitob", "dastur", "AI", "hello", "python"]
filtrlangan = []

for soz in sozlar:
    if len(soz) > 5:
        filtrlangan.append(soz)

print(filtrlangan)
