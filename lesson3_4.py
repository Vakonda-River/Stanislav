#x^(-y)=1/x^y
x_1 = float(input('Введите действительное положительное число: '))
y_1 = int(input('Введите целое отрицательное число: '))

def step(x,y):
    s = 1
    for i in range(abs(y)):
        s *= x
    res = 1/s
    return (res)

print(step(x_1,y_1))






