import requests
import encodings
b = requests.get('http://tech.emercit.com')

with open('11.txt', encoding= 'utf-8') as bb:

    for x in bb.readlines():
        post = open('53111.txt', 'w')
        #print(x.strip().split()[0])
        a = requests.get('http://emercit.com/tech3/log.php?bb=' + str(x.strip().split()[0]))
        post.write(a.text)
        post.close()

#print(a.status_code)
#print(a.headers)
#print(a.text)
#print(b.text)
