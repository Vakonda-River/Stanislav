txt = input("Введите несколько слов через пробел : ").split()
for txt, el in enumerate (txt):
    print("Строка",txt+1,":",''.join(el[:10]))






