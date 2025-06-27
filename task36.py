sozlar = ["kitob", "assalomu", "salom", "dasturlash", "AI"]

eng_uzun = ""
for soz in sozlar:
    if len(soz) > len(eng_uzun):
        eng_uzun = soz

print(eng_uzun)
