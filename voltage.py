import requests
import re
import region
a = requests.get('http://tech.emercit.com/state.html')
station_warning = {}
with open('1.txt','w',  encoding='UTF-8') as bb:
    bb.write(a.text.strip())
with open('1.txt', 'r', encoding='UTF-8') as vl:
    b = open('2.txt', 'a', encoding='UTF-8' )
    number_complex = []
    number_bb = []
    post = {}
    for x in vl:
        c = re.findall(r'АГК-....', str(x))
        d = re.findall(r'<td>............</td>', str(x))

        if c != []:
            for y in c:
                number_complex.append(y)
        if d != []:
            for x in d:
                number_bb.append(x[4:-5])

    for i in range(len(number_complex)):
        post[number_complex[i]] = number_bb[i]
        b.write(str(number_bb[i]) + ' ' + '-------->' + ' ' + str(number_complex[i]) + '\n')
    b.close()

    result = open('3.txt', 'a', encoding='UTF-8')
    low_voltage = open('danger.txt','a', encoding='UTF-8')
    chetchik = 0
    chetchik3 = 0
    for z in range(len(number_complex)):
        volt = requests.get('http://emercit.com/tech3/log.php?bb=' + str(number_bb[z]))
        data = re.findall(r'volt\(main=.....', str(volt.content))

        if data != [] and float(data[-2][-5:]) <= 12.0:
            if data[-1][-5:] not in station_warning.keys():
                station_warning[data[-2][-5:]] = number_complex[z]
            else:
                station_warning[data[-2][-5:]+ ' '*chetchik3] = number_complex[z]
            low_voltage.write(str(number_complex[z]) + '-------->' + str(data[-1])[-5:] + '\n')
            chetchik3 += 1
        elif data != []:
            result.write(str(number_bb[z]) + ' ' + '-------->' + ' ' + str(number_complex[z]) + ' ' + '-------->' + ' ' + str(data[-1])[-5:] + '\n')
        else:
            result.write(str(number_bb[z]) + ' ' + '-------->' + ' ' + str(number_complex[z]) + ' ' + '-------->' + ' ' + 'нет данных' + '\n')
            if 'нет данных' not in  station_warning.keys():
                station_warning['нет данных'] = number_complex[z]
            else:
                station_warning['нет данных'+ (" " * chetchik3)] = number_complex[z]
            continue
    result.close()

    low_sorted = open('low_sorted.txt', 'a' , encoding="UTF-8")
    for k in sorted(station_warning.keys()):

        nomer_agk = int(str(station_warning[k])[4:])
        #print(str(nomer_agk))
        print(station_warning[k], '-------->', k)
        for i in region.dict_r.keys():
            for j in region.dict_r[i]:
                if int(j) == nomer_agk:
                    print(str(station_warning[k]) + ' ' + '-------->' + ' '+  str(k) + str(i) + '\n')
                    low_sorted.write(str(station_warning[k]) + ' ' + '-------->' + ' '+  str(k) + ' '+ str(i) + '\n')


    low_sorted.close()
