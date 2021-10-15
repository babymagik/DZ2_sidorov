print(type(15 * 3)
print(type(15 / 3)
print(type(15 ** 2)
print(type(15 // 2)



list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in list:
    print('Привет', position.split()[-1].capitalize())



goods = [57.8, 46.51, 97, 152, 53, 1020.99, 212.22, 666.66, 808, 404.40 ]
for good in goods:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп')



goods = [57.8, 46.51, 97, 152, 53, 1020.99, 212.22, 666.66, 808, 404.40 ]
for good in sorted(goods)[::-1][:5]:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп')
