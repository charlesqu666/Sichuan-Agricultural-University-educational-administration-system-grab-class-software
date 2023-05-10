x=input('xuehao')
m=input('mm')
import random
m='1'+m
if m[-1]=='.':
    m=m.replace('.','')
    kami = str(random.randint(10000, 99999)) + str(int(x[2:999]) * 3) + str(random.randint(10000, 99999)) + str( int(m) * 9)+'.'
    print(kami)
else:
    kami = str(random.randint(10000, 99999)) + str(int(x[2:999]) * 3) + str(random.randint(10000, 99999)) + str( int(m) * 9)
    print(kami)



print('----------------'*10)



zhanghao='20'+str(int(kami[5:12])//3)
print(zhanghao)
if kami[-1]=='.':
    kami = kami.replace('.', '')
    mima1 = str(int(kami[17:999]) // 9)
    mima = mima1[1:999]+'.'
else:
    mima1 = str(int(kami[17:999]) // 9)
    mima=mima1[1:999]



print('mima',mima)
