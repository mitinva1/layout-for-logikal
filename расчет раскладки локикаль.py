# -*- coding: utf-8 -*-
while True:
    print("введите следующие параметры")
    h_prof = float(input("высота профиля рамы: "))
    w_r = float(input('ширина раскладки: '))
    q_r = int(input('колличество профилей раскладки: '))
    z_x = float(input('габаритный размер по раме: '))
    
    def xxx(h_prof,w_r,q_r,z_x):
        h_prof = h_prof
        w_r = w_r
        q_r = q_r
        z_x = z_x
        h_all = ((z_x-h_prof-h_prof)-(q_r*w_r))/(q_r+1)
        h_central = h_all + w_r
        h1 = round((h_all + h_prof + (w_r/2)), 1)
        z = []
        for x in range(q_r):
            z.append(h1)
            h1+=h_central
        return z
    z = xxx(h_prof,w_r,q_r,z_x)
    print('размеры: {0}\n'.format(z))


    
