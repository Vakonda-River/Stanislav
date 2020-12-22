txt1 = "Введите число :"
txt2 = "Самая большая цифра в числе = "

a = []
a = input (txt1)
n = 0;
max = int(a[n])
while n < len(a):
    m = int(a[n])
    if m > max:
        max = m
    n += 1
print (txt2 , max)








