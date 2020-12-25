my_list = [7,5,3,3,2]
print("Заданные условия:",my_list)
while True:
    new_el = int(input("Введите новый элемент :"))
    print("Вы ввели:",new_el)
    j=len(my_list); print(" размер листа ",j)
    poz = 0

    for i in range(j):
        if new_el == my_list[i]:
            poz = i+1
        if new_el < my_list[i]:
            poz = i+1
    my_list.insert(poz,new_el)
    print("Результат:",my_list)






