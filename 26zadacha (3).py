s = input()
total_kop = len(s) * 40
rub = total_kop // 100
kop = total_kop % 100
print(str(rub) + " р. " + str(kop) + " коп.")