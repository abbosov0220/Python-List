list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

umumiy = []

for element in list1:
    if element in list2 and element not in umumiy:
        umumiy.append(element)

print(umumiy)
