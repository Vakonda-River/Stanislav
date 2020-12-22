while True:
    a = input('Введите секунды для пересчёта : ')
    if a == 'stop':
        print('END')
        break
    t = int(a)
    th = t // 3600
    th_rep = t % 3600
    tm = th_rep // 60
    tm_rep = th_rep % 60
    print('Часов : ', th, '  Минут : ', tm, '  Секунд : ', tm_rep)
    print ('Для остановки введите "stop"')
