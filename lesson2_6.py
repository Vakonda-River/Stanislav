print("Учёт товаров.")
n = int(input("Укажите количество товаров для учета:"))
sklad = []
key = ["Наименование:","Цена:","Количество:"]
for i in range(n):
    sklad.append(input("Введите код позиции:"))
    dic = {}
    for j in range(len(key)):
        val = input(key[j])
        dic[key[j]] = val
    sklad.append(dic)
    i+=2
print(sklad)


