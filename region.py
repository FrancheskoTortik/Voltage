import re
#import voltage as vl
temp_reg = []
chek3 = 0

with open('3333.txt', 'r', encoding='UTF-8')as data:

    for i in data.readlines():
        reg = re.findall(r'\w+\sрайон', i)

        temp = 0
        if reg != [] and 'Лазаревский район' not in reg and 'Адлерский район' not in reg and 'Хостинский район' not in reg and 'Центральный район' not in reg:
            for x in reg:
                temp_reg.append(x)
  #создаем пустой словарь и наполняем его Район: [АГК]
temp_file = open('temp_file.txt', 'a', encoding='UTF-8')
with open('3333.txt', 'r', encoding='UTF-8')as data:
    dict_reg = {}
    for i in data.readlines():
        reg = re.findall(r'\w+\sрайон', i)
        reg2 = re.findall(r'\d+', i)
        if reg != [] and 'Лазаревский район' not in reg and 'Адлерский район' not in reg and 'Хостинский район' not in reg and 'Центральный район' not in reg:
            for x in reg:
                temp_file.write(x + '\n')
                #chek +=1
                dict_reg[x] = 1
        if reg2 != []:
            for y in reg2:
                temp_file.write(y + "\n")

temp_file.close()
#print(chek, sorted(temp_reg))
dict_reg = []
dict_r = {}
temp_param = 0
#наполняем словарь стациями
with open('temp_file.txt', 'r', encoding='UTF-8') as file:
    for x in file.readlines():
        dict_reg.append(x.strip())
#print(dict_reg)
for x in dict_reg:
    if len(str(x)) > 6:
        temp_param1 = x
        #print(temp_param1)
        dict_r[temp_param1] = []
        #dict_reg.remove(x)

    else:
        dict_r[temp_param1].append(int(x))

regiony_resalt = open('regiony_result.txt' , 'a' , encoding='UTF-8')
#print(dict_r.keys())
#print(dict_r.values())
for i in dict_r.keys():
    for j in dict_r[i]:
        regiony_resalt.write(str(i)+ " " + str(j)+ '\n')

regiony_resalt.close()