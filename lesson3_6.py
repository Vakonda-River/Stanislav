a_1 = input("Введите слово на латинице маленькими буквами: ")

def int_func(a):
    return (a.capitalize())

print('Слово изменено: ',int_func(a_1))

txt = input("Введите несколько слов на латинице маленькими буквами через пробел : ").split()

txt_new=[]
for i in range(len(txt)):
    txt_new.append(int_func(txt[i]))
strOf = ' '.join(txt_new)

print('Слова изменены: ',strOf)










