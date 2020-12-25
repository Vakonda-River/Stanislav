str = input("Введите  несколько цифр = ")
print("Ввели последовательность:",str)
delt = len(str)%2
str_list = list(str)
l = len(str_list)
idx = 0
if delt == 0:
    idx = 1
else:
    idx = 2
i=0
while i<(len(str_list)-idx):
    str_list[i], str_list[i+1] = str_list[i+1], str_list[i]
    i+=2
print("Результат  сортировки   :","".join(str_list))







