import tkinter as tk
import re
import requests
import threading
from tkinter import messagebox


root=tk.Tk()
root.title('查氏抢课')
root.geometry('500x400')


################################# 参数设置 ###############################################

zhanghao=''
mima=''
result=tk.StringVar()
how=0
list=''
sign=''
hourkey=''
list1=''
when=''
no11=''
no21=''
no31=''
no41=''
no51=''
no61=''
no71=''
no81=''
no12=''
no22=''
no32=''
no42=''
no52=''
no62=''
no72=''
no82=''
listkind=''
listnow=''
dic={}
kebian=''
show_bianhao=tk.StringVar()
kai=''
temp=''
bh=''
dic=''
pr1=''
pr2=''
pr3=''
pr4=''
pr5=''
pshu=0
################################ 函数 ##########################################

def x():
    global kami
    global zhanghao
    global mima
    global how

    kami=e1.get()
    print(kami)
    if len(kami)>12:
        zhanghao = '20' + str(int(kami[5:12]) // 3)
        if kami[-1] == '.':
            kami = kami.replace('.', '')
            mima1 = str(int(kami[17:999]) // 9)
            mima = mima1[1:999] + '.'
        else:
            mima1 = str(int(kami[17:999]) // 9)
            mima = mima1[1:999]
        y = '欢迎你,' + zhanghao + '\n欢迎使用本系统'
        result.set(y)

        print(kami)
        print('zhanghao', zhanghao)
        print('mima', mima)
        how=1


    else:
        pass

def b20():
    global how
    global list1
    global list
    global result
    global sign
    global hourkey
    if how==1:
        url = 'https://jiaowu.sicau.edu.cn/'
        headers = {'Host': 'jiaowu.sicau.edu.cn',
                   'Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'Accept-Encoding': 'gzip, deflate',
                   'Sec-Fetch-Site': 'none',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
                   'Accept-Language': 'zh-CN,zh;q=0.9'
                   }

        frist = requests.get(url, headers=headers, allow_redirects=False)
        print('first1'+str(frist.text))
        frist1 = frist.cookies
        print('frist1cookie'+str(frist1))
        list1 = requests.utils.dict_from_cookiejar(frist1)
        list10 = list1
        list1 = str(list1)
        list1 = list1.replace('{', '')
        list1 = list1.replace('}', '')
        list1 = list1.replace(':', '=')
        list1 = list1.replace(' ', '')
        list1 = list1.replace("'", "")
        print(list1)

        print('--------------' * 10)

        url = 'https://jiaowu.sicau.edu.cn/web/web/web/index.asp'
        headers = {'Host': 'jiaowu.sicau.edu.cn',
                   'Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Sec-Fetch-Site': 'none',
                   'Sec-Fetch-Mode': 'navigate',
                   'Sec-Fetch-Dest': 'document',
                   'Sec-Fetch-User': '?1',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Cookie': list1
                   }

        fristtiao = requests.get(url, headers=headers)

        s1 = fristtiao.text

        print('frist2'+str(s1))

        # 处理sign
        sign = re.search('sign" value="(.*?)"', s1).group(1)

        print(sign)
        # 处理hourkey
        #############
        hourkey = re.search('hour_key" value="(.*?)"', s1).group(1)
        print(hourkey)

        how=2
        if str(fristtiao)=='<Response [200]>':
           m=result,'\n第一步已经完成'
        else:m=result,'\n出现未知错误'
        result.set(m)
    else: m='请按照步骤执行'
    result.set(m)

def b30():
    global how
    global sign
    global hourkey
    global zhanghao
    global mima
    global list
    if how==2:
        url = 'https://jiaowu.sicau.edu.cn/jiaoshi/bangong/check.asp'
        headers = {'Host': 'jiaowu.sicau.edu.cn',
                   'Connection': 'keep-alive',
                   'Content-Length': '231',
                   'Cache-Control': 'max-age=0',
                   'Upgrade-Insecure-Requests': '1',
                   'Origin': 'https://jiaowu.sicau.edu.cn',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                   'Referer': 'https://jiaowu.sicau.edu.cn/web/web/web/index.asp',
                   'Accept-Encoding': 'gzip, deflate,br',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Sec-Fetch-Site': 'same-origin',
                   'Sec-Fetch-Mode': 'navigate',
                   'Sec-Fetch-Dest': 'document',
                   'Sec-Fetch-User': '?1',
                   'Cookie': list1,
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
                   }


        data='user='+str(zhanghao)+'&pwd='+str(mima)+'&lb=S&submit=&sign='+str(sign)+'&hour_key='+str(hourkey)
        k = requests.post(url, data=data, headers=headers, allow_redirects=False)
        print('k'+str(k.text))


        headers={'Host': 'jiaowu.sicau.edu.cn',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Referer': 'https://jiaowu.sicau.edu.cn/web/web/web/index.asp',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': list1}

        url='https://jiaowu.sicau.edu.cn/jiaoshi/bangong/main/index1.asp'
        second = requests.get(url, headers=headers, allow_redirects=True)
        second1 = second.cookies
        list2 = requests.utils.dict_from_cookiejar(second1)
        list20 = list2
        list2 = str(list2)
        list2 = list2.replace('{', '')
        list2 = list2.replace('}', '')
        list2 = list2.replace(':', '=')
        list2 = list2.replace(' ', '')
        list2 = list2.replace("'", "")
        list = list1 + ',' + list2

        print(k.cookies)
        print(sign)
        m=result,'\n第二步已经完成'
        if str(second)== '<Response [200]>':
            how=3
            m = result, '\n第二步已经完成'
        else:m=result,'\n出现错误,可能是卡密错了'
        result.set(m)
    else:m='请按照步骤执行'
    result.set(m)

def b40():
        global list
        global list1
        global how
        if how==3:

            url = 'https://jiaowu.sicau.edu.cn/jiaoshi/bangong/main/welcome1.asp'
            headers = {'Host': 'jiaowu.sicau.edu.cn',
                       'Connection': 'keep-alive',
                       'Upgrade-Insecure-Requests': '1',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                       'Referer': 'https://jiaowu.sicau.edu.cn/jiaoshi/bangong/main/index1.asp',
                       'Accept-Encoding': 'gzip, deflate',
                       'Cookie': list
                       }

            second2 = requests.get(url, headers=headers, allow_redirects=True)
            second2 = second2.cookies
            list3 = requests.utils.dict_from_cookiejar(second2)
            lis30 = list3
            print(list3)
            list3 = str(list3)
            list3 = list3.replace('{', '')
            list3 = list3.replace('}', '')
            list3 = list3.replace(':', '=')
            list3 = list3.replace(' ', '')
            list3 = list3.replace("'", "")
            list = list + ',' + list3

            url = 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/bxq.asp'

            headers = {'Host': 'jiaowu.sicau.edu.cn',
                       'Connection': 'keep-alive',
                       'Upgrade-Insecure-Requests': '1',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                       'Referer': 'https://jiaowu.sicau.edu.cn/jiaoshi/bangong/main/index1.asp',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Cookie': list
                       }

            second30 = requests.get(url, headers=headers, allow_redirects=True)
            second3 = second30.cookies
            list4 = requests.utils.dict_from_cookiejar(second3)
            list40 = list4
            list4 = str(list4)
            list4 = list4.replace('{', '')
            list4 = list4.replace('}', '')
            list4 = list4.replace(':', '=')
            list4 = list4.replace(' ', '')
            list4 = list4.replace("'", "")
            list = list + ',' + list4
            print('------' * 10)
            print(list)
            if str(second30=='<Response [200]>'):
             m=result,'\n第三步已经完成'
             how=4
            else: m=result,'\n出现未知错误,\n可能是卡密不对\n也可能是校园服务器故障'
            result.set(m)
        else :m='请按照步骤执行'
        result.set(m)

def b50():
    global when
    global how
    global list
    global no11
    global no12
    global no21
    global no22
    global no31
    global no32
    global no41
    global no42
    global no51
    global no52
    global no61
    global no62
    global no71
    global no72
    global no81
    global no82
    global listkind
    if how==4:
        url1 = 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/xszhinan.asp?title_id1=9&xueqi='
        when = e2.get()
        url = url1 + when
        headers = {'Referer': 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/bxq.asp',
                   'Host': 'jiaowu.sicau.edu.cn',
                   'Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Cookie': list
                   }

        third = requests.get(url, headers=headers, allow_redirects=True)
        third = third.cookies
        list5 = requests.utils.dict_from_cookiejar(third)
        print(list5)
        list50 = list5
        list5 = str(list5)
        list5 = list5.replace('{', '')
        list5 = list5.replace('}', '')
        list5 = list5.replace(':', '=')
        list5 = list5.replace(' ', '')
        list5 = list5.replace("'", "")
        list = list + ',' + list5

        url = 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kai.asp?title_id1=2'
        headers = {'Referer': url1,
                   'Host': 'jiaowu.sicau.edu.cn',
                   'Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Cookie': list
                   }

        third1 = requests.get(url, headers=headers, allow_redirects=True)
        what = third1.text
        third1 = third1.cookies
        list6 = requests.utils.dict_from_cookiejar(third)
        print(list6)
        list60 = list6
        list6 = str(list6)
        list6 = list6.replace('{', '')
        list6 = list6.replace('}', '')
        list6 = list6.replace(':', '=')
        list6 = list6.replace(' ', '')
        list6 = list6.replace("'", "")
        listkind = list + ',' + list6
        print(list6)
        kairaw = re.findall('kai=\d+&temp=\d+', what)
        d = ' '.join(kairaw)
        no11 = re.search('kai=(\d+)&temp=(\d+)', d).group(1)
        no12 = re.search('kai=(\d+)&temp=(\d+)', d).group(2)
        no10 = re.search('kai=(\d+)&temp=(\d+)', d).group(0)
        d = d.replace(no10, '')
        no21 = re.search('kai=(\d+)&temp=(\d+)', d).group(1)
        no22 = re.search('kai=(\d+)&temp=(\d+)', d).group(2)
        no20 = re.search('kai=(\d+)&temp=(\d+)', d).group(0)
        d = d.replace(no20, '')
        no31 = re.search('kai=(\d+)&temp=(\d+)', d).group(1)
        no32 = re.search('kai=(\d+)&temp=(\d+)', d).group(2)
        no30 = re.search('kai=(\d+)&temp=(\d+)', d).group(0)
        d = d.replace(no30, '')
        no41 = re.search('kai=(\d+)&temp=(\d+)', d).group(1)
        no42 = re.search('kai=(\d+)&temp=(\d+)', d).group(2)
        no40 = re.search('kai=(\d+)&temp=(\d+)', d).group(0)
        d = d.replace(no40, '')
        no51 = re.search('kai=(\d+)&temp=(\d+)', d).group(1)
        no52 = re.search('kai=(\d+)&temp=(\d+)', d).group(2)
        no50 = re.search('kai=(\d+)&temp=(\d+)', d).group(0)
        d = d.replace(no50, '')
        no61 = re.search('kai=(\d+)&temp=(\d+)', d).group(1)
        no62 = re.search('kai=(\d+)&temp=(\d+)', d).group(2)
        no60 = re.search('kai=(\d+)&temp=(\d+)', d).group(0)
        d = d.replace(no60, '')
        no71 = re.search('kai=(\d+)&temp=(\d+)', d).group(1)
        no72 = re.search('kai=(\d+)&temp=(\d+)', d).group(2)
        no70 = re.search('kai=(\d+)&temp=(\d+)', d).group(0)
        d = d.replace(no70, '')
        no81 = re.search('kai=(\d+)&temp=(\d+)', d).group(1)
        no82 = re.search('kai=(\d+)&temp=(\d+)', d).group(2)
        no80 = re.search('kai=(\d+)&temp=(\d+)', d).group(0)
        d = d.replace(no80, '')
        m=result,'\n已经接受到请求'
        result.set(m)

    else :m='请按照步骤执行'
    result.set(m)

def b60():
    global listkind
    global listnow
    global result
    global how
    global kai
    global temp
    global dic

    smkindke=e3.get()

    if smkindke == '1':
        no1=no11
        no2=no12
    else:
        if smkindke == '2':
            no1 = no21
            no2 = no22
        else:

            if smkindke == '3':
                no1 = no31
                no2 = no32
            else:
                if smkindke == '4':
                    no1 = no41
                    no2 = no42
                else:
                    if smkindke == '5':
                        no1 = no51
                        no2 = no52
                    else:
                        if smkindke == '6':
                            no1 = no61
                            no2 = no62
                        else:
                            if smkindke == '7':
                                no1 = no71
                                no2 = no72
                            else:
                                if smkindke =='8':
                                    no1 = no81
                                    no2 = no82
                                else:
                                    if smkindke == '9':
                                        no1 = no81
                                        no2 = no82
                                    else:
                                        m = '请正确输入'



                                    result.set(m)

    url = 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kaike.asp'
    headers = {
        'Referer': 'Referer: https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kai.asp?title_id1=2',
        'Host': 'jiaowu.sicau.edu.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': listkind
    }
    pa = {'title_id1': '2', 'kai': no1, 'temp': no2}
    kai=no1

    temp=no2

    third2 = requests.get(url=url, headers=headers, params=pa)
    what1 = third2.text
    third2 = third2.cookies
    list7 = requests.utils.dict_from_cookiejar(third2)
    print(list7)
    list70 = list7
    list7 = str(list7)
    list7 = list7.replace('{', '')
    list7 = list7.replace('}', '')
    list7 = list7.replace(':', '=')
    list7 = list7.replace(' ', '')
    list7 = list7.replace("'", "")
    listnow = listkind + ',' + list7

    kecbianhaoshi = re.findall('bianhao=(\d+)">', what1)
    kewaishi = re.findall('align=left >(\w+)</td><t', what1)
    print(kecbianhaoshi)
    print(kewaishi)

    # 1
    kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
    kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
    kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
    kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
    while len(kewai1) !=9:
        what1 = what1.replace(kewai2, '')
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)

    what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
    dic = {kewai1: kecbianhao1}

    # 2
    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        sss = 'sss'
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)

    kjianc = re.search('bianhao=(\d+)">', what1)
    if kjianc == None:
        print('全部课程加载完毕')
    else:
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewaishi = re.findall('align=left >(\w+)</td><t', what1)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic1 = {kewai1: kecbianhao1}
        dic.update(dic1)
        how=8

    print(dic)
    dictbianhao=dic.keys()
    show_bianhao.set(dictbianhao)
    print(dic)







##############################################################






def b70():
    global how
    global result
    global list
    global kai
    global temp
    global bh
    global dic


    if how==8:
        yeshu=e5.get()
        url='https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kaike.asp?title_id1=2&kai='
        kai = str(kai)
        temp = str(temp)
        url=url+kai+'&temp='+temp
        headers = {
            'Referer': url,
            'Host': 'jiaowu.sicau.edu.cn',
            'Connection': 'keep-alive',
            'Cache-Control':'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Origin':'https://jiaowu.sicau.edu.cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': list
        }
        data={'y':yeshu,
              'bh':bh
        }
        p=requests.post(url=url,headers=headers,data=data)
        what1 = p.text


        kecbianhaoshi = re.findall('bianhao=(\d+)">', what1)
        kewaishi = re.findall('align=left >(\w+)</td><t', what1)
        print(kecbianhaoshi)
        print(kewaishi)

        # 1
        kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
        kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
        kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
        kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
        while len(kewai1) !=9:
            what1 = what1.replace(kewai2, '')
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)

        what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
        dic = {kewai1: kecbianhao1}

        # 2
        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            sss = 'sss'
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9:
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        kjianc = re.search('bianhao=(\d+)">', what1)
        if kjianc == None:
            print('全部课程加载完毕')
        else:
            kecbianhao1 = re.search('bianhao=(\d+)">', what1).group(1)
            kecbianhao2 = re.search('bianhao=(\d+)">', what1).group(0)
            kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
            kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            while len(kewai1) !=9 :
                what1 = what1.replace(kewai2, '')
                kewaishi = re.findall('align=left >(\w+)</td><t', what1)
                kewai1 = re.search('align=left >(\w+)</td><t', what1).group(1)
                kewai2 = re.search('align=left >(\w+)</td><t', what1).group(0)
            what1 = what1.replace(kecbianhao2, '', ).replace(kewai2, '')
            dic1 = {kewai1: kecbianhao1}
            dic.update(dic1)

        print(dic)
        dictbianhao = dic.keys()
        show_bianhao.set(dictbianhao)
        print(dic)


    else:m='请按照步骤操作'
    result.set(m)

def pro1():
    global dic
    global pr1
    global result
    thing=epro1.get()
    if dic.get(thing)==None:
        m='无法查询到此课'
        result.set(m)
    else:
        pr1=dic.get(thing)
        m='准备成功'
        result.set(m)
    print(pr1)


def pro2():
    global dic
    global pr2
    global result
    thing=epro2.get()
    if dic.get(thing)==None:
        m='无法查询到此课'
        result.set(m)
    else:
        pr2=dic.get(thing)
        m='准备成功'
        result.set(m)
    print(pr2)


def pro3():
    global dic
    global pr3
    global result
    thing=epro3.get()
    if dic.get(thing)==None:
        m='无法查询到此课'
        result.set(m)
    else:
        pr3=dic.get(thing)
        m='准备成功'
        result.set(m)
    print(pr3)


def pro4():
    global dic
    global pr4
    global result
    thing=epro4.get()
    if dic.get(thing)==None:
        m='无法查询到此课'
        result.set(m)
    else:
        pr4=dic.get(thing)
        m='准备成功'
        result.set(m)
    print(pr4)


def pro5():
    global dic
    global pr5
    global result
    thing=epro5.get()
    if dic.get(thing)==None:
        m='无法查询到此课'
        result.set(m)
    else:
        pr5=dic.get(thing)
        m='准备成功'
        result.set(m)
    print(pr5)




def pp1():
    global pr1
    global listnow
    global result
    url = 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/xuan_2018.asp'
    headers = {
        'Referer': 'Referer: https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kai.asp?title_id1=2',
        'Host': 'jiaowu.sicau.edu.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': listnow
    }

    paa = {'bianhao':pr1}
    m = result.get()+'\n1号线程添加成功'
    result.set(m)
    finall = requests.get(url, headers=headers, params=paa)
    print(finall.text)





def qiang1():
    global pr1
    global result
    if pr1 == '':
        m = '请先提前加载'
        result.set(m)
    else:
        add_thread = threading.Thread(target=pp1)
        add_thread.start()

def pp2():
    global pr2
    global listnow
    global result
    url = 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/xuan_2018.asp'
    headers = {
        'Referer': 'Referer: https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kai.asp?title_id1=2',
        'Host': 'jiaowu.sicau.edu.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': listnow
    }

    paa = {'bianhao':pr2}
    m = result.get()+'\n2号线程添加成功'
    result.set(m)
    finall = requests.get(url, headers=headers, params=paa)
    print(finall.text)




def qiang2():
    global pr2
    global result
    if pr2 == '':
        m = '请先提前加载'
        result.set(m)
    else:
        add_thread = threading.Thread(target=pp2)
        add_thread.start()




def pp3():
    global pr3
    global listnow
    global result
    url = 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/xuan_2018.asp'
    headers = {
        'Referer': 'Referer: https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kai.asp?title_id1=2',
        'Host': 'jiaowu.sicau.edu.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': listnow
    }

    paa = {'bianhao':pr3}
    m = result.get()+'\n3号线程添加成功'
    result.set(m)
    finall = requests.get(url, headers=headers, params=paa)
    print(finall.text)




def qiang3():
    global pr3
    global result
    if pr3 == '':
        m = '请先提前加载'
        result.set(m)
    else:
        add_thread = threading.Thread(target=pp3)
        add_thread.start()



def pp4():
    global pr4
    global listnow
    global result
    url = 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/xuan_2018.asp'
    headers = {
        'Referer': 'Referer: https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kai.asp?title_id1=2',
        'Host': 'jiaowu.sicau.edu.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': listnow
    }

    paa = {'bianhao':pr4}
    m = result.get()+'\n4号线程添加成功'
    result.set(m)
    finall = requests.get(url, headers=headers, params=paa)
    print(finall.text)




def qiang4():
    global pr4
    global result
    if pr4 == '':
        m = '请先提前加载'
        result.set(m)
    else:
        add_thread = threading.Thread(target=pp4)
        add_thread.start()

def pp5():
    global pr5
    global listnow
    global result
    url = 'https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/xuan_2018.asp'
    headers = {
        'Referer': 'Referer: https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kai.asp?title_id1=2',
        'Host': 'jiaowu.sicau.edu.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': listnow
    }

    paa = {'bianhao':pr5}
    m = result.get()+'\n5号线程添加成功'
    result.set(m)
    finall = requests.get(url, headers=headers, params=paa)
    print(finall.text)




def qiang5():
    global pr5
    global result
    if pr5 == '':
        m = '请先提前加载'
        result.set(m)
    else:
        add_thread = threading.Thread(target=pp5)
        add_thread.start()




def clearall():
    global result
    m=''
    result.set(m)







import os
import webbrowser





def p1c():
    global pshu
    pshu=1

    top=tk.Toplevel()
    top.title('好奇心这么重干嘛？')
    top.geometry('200x100')
    l=tk.Label(top,text='不是说了没用吗，还点。')
    l.place(x=30,y=40)


def p2c():
    global pshu
    pshu=2

    top=tk.Toplevel()
    top.title('好奇心这么重干嘛？')
    top.geometry('200x100')
    l=tk.Label(top,text='还点！')
    l.place(x=30,y=40)


def p3c():
    global pshu
    pshu = 3

    top = tk.Toplevel()
    top.title('好奇心这么重干嘛？')
    top.geometry('200x100')
    l = tk.Label(top, text='再点试试！')
    l.place(x=30, y=40)



import random





def p4c():
    root1=tk.Tk()
    root1.title('你摊上事了')
    root1.geometry('300x200+500+300')
    import random

    def quit():
        root1.quit()


    def show():
        tuichu=tk.Button(root1,text='退出',command=quit)
        tuichu.place(x=180,y=120)

    def open():
        url = 'https://space.bilibili.com/345560267'

        webbrowser.open(url)
        show()



    ag=tk.Button(root1,text='好的',bd=0,font='黑体',fg='green',command=open)
    ag.place(x=80,y=120)

    da=tk.Button(root1,text='不好',bd=0,font='黑体',fg='red')
    da.place(x=180,y=120)

    t=tk.Label(root1,text='去给作者三连好不好')
    t.place(x=90,y=50)

    def butong():
        messagebox.showwarning(title='提示',message='此路不通')
    root1.protocol('WM_DELETE_WINDOW',butong)

    l=1

    while l<1:
        x1 = random.randint(10, 270)
        y1 = random.randint(10, 170)




    def move(event):


        x1 = random.randint(10, 270)
        y1 = random.randint(10, 170)

        da.place(x=x1,y=y1)


    da.bind('<Enter>',move)






def jianchapishu():
    global pshu
    if pshu==0:
        p1c()
    else:
        if pshu==1:
            p2c()
        else:
            if pshu==2:
               p3c()
            else:
                 if pshu==3:
                     p4c()
                 else:
                     pass




def help():
    url='https://pv5oo4ve3f.feishu.cn/docs/doccntoGMRbcpGJfcVl3PxCQQCe'
    webbrowser.open(url)
    messagebox.showinfo(title='提示', message='立马为您打开帮助文档')

def who():
    messagebox.showwarning(title='什么',message='你不认识作者吗？请立即关闭此软件')

def new():
    messagebox.showwarning(title='更新内容',message='1.更新了对学校网站的新适配（2022.6.30）')







################################ 布局 ####################################################


clear=tk.Button(root,text='清空消息栏',command=clearall)
clear.place(x=370,y=350)


e1=tk.Entry(root)
e1.place(x=90,y=12)



b1=tk.Button(root,text='加载卡密',command=x)
b1.place(x=250,y=9)


l1=tk.Label(root,text='请输入卡密:')
l1.place(x=10,y=10)



lxiang=tk.Label(root,bg='#FFFFCC',height=20,width=20)
lxiang.place(x=330,y=9)
lxiang1=tk.Label(root,textvariable=result,height=20,width=19,anchor='nw')
lxiang1.place(x=333,y=13)


b2=tk.Button(root,text='第一步',command=b20)
b2.place(x=10,y=40 )

b3=tk.Button(root,text='第二步',command=b30)
b3.place(x=80,y=40 )

b4=tk.Button(root,text='第三步',command=b40)
b4.place(x=150,y=40)


e2=tk.Entry(root)
e2.place(x=90,y=80)

b5=tk.Button(root,text='获取列表',command=b50)
b5.place(x=250,y=77)

l2=tk.Label(root,text='输入学期:')
l2.place(x=10,y=80)

l3=tk.Label(root,text='输入某类课:')
l3.place(x=10,y=120)

e3=tk.Entry(root)
e3.place(x=90,y=120)

b6=tk.Button(root,text='获取列表',command=b60)
b6.place(x=250,y=117)

e4=tk.Entry(root,textvariable=show_bianhao)
e4.place(x=90,y=160)

l4=tk.Label(root,text='获取到的编号:')
l4.place(x=10,y=160)

e5=tk.Entry(root)
e5.place(x=90,y=200)

l5=tk.Label(root,text='跳转到：')
l5.place(x=10,y=200)


b7=tk.Button(root,text='跳转',command=b70)
b7.place(x=250,y=197)


epro1=tk.Entry(root)
epro1.place(x=10,y=240)

bpro1=tk.Button(root,text='加载',command=pro1)
bpro1.place(x=170,y=237)

epro2=tk.Entry(root)
epro2.place(x=10,y=267)

bpro2=tk.Button(root,text='加载',command=pro2)
bpro2.place(x=170,y=267)

epro3=tk.Entry(root)
epro3.place(x=10,y=300)

bpro3=tk.Button(root,text='加载',command=pro3)
bpro3.place(x=170,y=297)

epro4=tk.Entry(root)
epro4.place(x=10,y=330)

bpro4=tk.Button(root,text='加载',command=pro4)
bpro4.place(x=170,y=327)

epro5=tk.Entry(root)
epro5.place(x=10,y=360)

bpro5=tk.Button(root,text='加载',command=pro5)
bpro5.place(x=170,y=357)

bq1=tk.Button(root,text='添加线程',command=qiang1)
bq1.place(x=240,y=237)

bq2=tk.Button(root,text='添加线程',command=qiang2)
bq2.place(x=240,y=267)

bq3=tk.Button(root,text='添加线程',command=qiang3)
bq3.place(x=240,y=297)

bq4=tk.Button(root,text='添加线程',command=qiang4)
bq4.place(x=240,y=327)

bq5=tk.Button(root,text='添加线程',command=qiang5)
bq5.place(x=240,y=357)

op=tk.Button(root,text='一个没什么用的按钮',command=jianchapishu)
op.place(x=343,y=317)

menu=tk.Menu(root)
menu.add_command(label='谁是作者',command=who)
menu.add_command(label='帮助',command=help)
menu.add_command(label='更新内容',command=new)
root.config(menu=menu)


root.mainloop()






