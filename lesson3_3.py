n = int(input('Укажите, сколько аргументов хотите ввести (не менее двух): '))

def sum_max(n):
    arg = []
    for i in range(n):
        a = float(input('Введите аргумент: '))
        arg.append(a)
    res = 0
    for i in range(2):
        n = 0
        max = float(arg[n])
        while n < len(arg):
            m = float(arg[n])
            if m > max:
                max = m
            n += 1
        res += max
        arg.remove(max)
    return (res)

print ('Сумма двух наибольших аргументов = ',sum_max(n))





