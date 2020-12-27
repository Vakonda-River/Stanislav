print('Пожалуйста,ниже введите Ваши личные данные.')
param_pers = ['Имя: ', 'Фамилия: ', 'Год рождения: ', 'Город проживания: ', 'email: ', 'Телефон: ']

def person(arg):
    dic_pers = {}
    for i in range(len(arg)):
        dic_pers[arg[i]] = input(arg[i])
    return (dic_pers)

sl = person(param_pers)
stroka = []
i=0
while i<len(param_pers):
    stroka.append(param_pers[i])
    stroka.append(sl[param_pers[i]])
    if i<(len(param_pers)-1):
        stroka.append(';')
    i += 1
print('Проверьте Ваши личные данные.')
print("  ".join(stroka),'.')



