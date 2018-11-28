import random
check = 0
sudo = [[0]*8 for i in range(8)]
sudo[3][5] = 5
sudo[2][6] = 3
sudo[4][5] = 4
sudo[5][5] = 7
sudo[1][2] = 2
sudo[7][2] = 1

#print(sudo)


# Начинаем заполнение таблицы
for i in range(8):
    for j in range(8):
        while check <= 58:
            if sudo[i][j] == 0:
                for x in range(1,9):
                    if x not in sudo[i]:
                        temp_list = []
                        for y in range(8):
                            temp_list.append(sudo[i][y])
                        if x not in temp_list:
                            sudo[i][j] = x
                            check +=1
                            print(check)
                        else:
                            continue

                            for i in range(8):
                                print(sudo[i])
                    else:
                        continue
            else:
                continue


                #sudo[i][j] = int(x)



    #print(sudo_2)
#print("Привет, мой друг! Введи количество известных чисел:")
#data_count = str(input())
