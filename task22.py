n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)

print("Введите элементы второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)

common_elements = sorted(set1.intersection(set2))
print (common_elements)
