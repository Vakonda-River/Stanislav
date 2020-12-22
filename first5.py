txt = "День тенировки номер"
rest = "Результат "
res_txt = "достигнут на "
ld = " km."
ans_d = "-й день."

l1 = 2
l2 = 3
day = 1
while True:
    delta = l1 * 0.1
    l1 += delta
    day += 1
    print (txt,day)
    print(rest,round(l1, 2),ld)
    if l1 >= l2:
        print (rest,res_txt,day,ans_d)
        break
