import sys

n = int(input('Пожалуйста, укажите точность результата (кол.во знаков после запятой : '))
def inpt_num():
    a = input('Введите  несколько цифр через пробел. Для выхода введите символ "/" :').split()
    for i in range(len(a)):
        if a[i] == '/':
            a[i] = str(a[i])
        else:
            a[i]=float(a[i])
    return (a)

def func():
    al = inpt_num()
    sum = 0
    if al != '':
        for i in range(len(al)):
            if type(al[i]) == float:
                sum += al[i]
            elif al[i] == '/':
                print('Сумма =', round((res + sum),n))
                print('Программа остановлена!')
                sys.exit()
    return (sum)

res = 0
while True:
    res += func()
    print('Сумма =', round(res,n))





