ins = "Введите число от 0 до 9 : "
fsp = "Вы ввели неверное значение, попробуйте еще раз"
sym_t = "Расчет суммы чисел :"
zp = ";"
res_t = "Сумма чисел :"

while True:
    n = input(ins)
    a = int(n)
    if (a < 0 or a > 9):
        print (fsp)
    else:
        break
b = int (n+n)
c = int (n+n+n)
print(sym_t, a, zp, b, zp, c )
print (res_t, (a+b+c))


