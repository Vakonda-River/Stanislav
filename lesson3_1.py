
as_1 = float(input('Введите делимое: '))
bs_1 = float(input('Введите делитель (число, отличное от нуля): '))

def delen(a,b):
       while True:
        if b == 0:
            return ('Вы пытались произвести деление на НОЛЬ! Это карается кармическим штрафом! Попробуйте еще раз!')
            break
        else:
            r = int(input('Укажите, до скольки знаков после запятой округлить результат: '))
            return (round((a/b),r))

print('Результат деления:',delen(as_1,bs_1))







