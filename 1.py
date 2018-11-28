import re
dict = {}
chek = 0
with open('3333.txt', 'r', encoding='UTF-8') as a:
    for i in a.readlines():
        temp_agk = []
        temp_rigion = []
        with open('4444.txt', 'a', encoding='UTF-8') as stations:
            #stations.write(i)
            if re.findall(r'МО', i):
                #print('Find IT!')
                continue
            elif re.findall(r'\d', i) == [] and re.findall(r'Сумма', i) == [] and re.findall(r'АГК', i) == [] and (re.findall(r'МО', i) == [] or re.findall(r'район', i)):
                chek =+1
                print('marker', temp_rigion, type(temp_rigion), chek)
                if i[:-2].strip() != '':
                    chek+=1
                    temp_rigion.append(i[:-2].strip())
                    print(type(temp_rigion),temp_rigion, chek)
                    for x in temp_rigion:
                        print(type(x))
                        stations.write(x + '\n')
                        print(temp_rigion, type(temp_rigion))
            elif re.findall(r'[\d]+', i):
                temp_agk = re.findall(r'[\d]+', i)
                for x in temp_agk:
                    stations.write(x + '\n')
                print(temp_agk, type(temp_agk))




