# ПРИНИМАЕТ ТОЛЬКО ЦЕЛЫЕ ЧИСЛА И ИГНОРИРУЕТ СИМВОЛЫ КРОМЕ СИМВОЛА ОКОНЧАНИЯ ПРОГРАММЫ
import sys

def inpt_num():
    a = input('Введите  несколько цифр через пробел. Для выхода введите символ "/" :').split()
    return (a)

def func():
    al = inpt_num()
    sum = 0
    if al != '':
        for i in range(len(al)):
            if al[i].isdigit() == True:
                sum += float(al[i])
            elif al[i].isdigit() == False:
                if al[i] == '/':
                    print('Сумма =', res + sum)
                    print('Программа остановлена!')
                    sys.exit()
                elif al[i] != '/':
                    print('Символ <', al[i], '> игнорирован')
    return (sum)

res = 0
while True:
    res += func()
    print('Сумма =', res)










