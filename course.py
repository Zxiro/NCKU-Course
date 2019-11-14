import requests #python提供的發送http請求的模組
from bs4 import BeautifulSoup #bs4為module名稱 Beautiful...為functionname
from time import sleep
import os

infoarray=[]
url = "http://course-query.acad.ncku.edu.tw/qry/qry001.php?dept_no="

pro=input('請輸入系所代碼:' )
print(pro)
num=input('請輸入課程代號:')
print(num)

url=url + pro

resp = requests.get(url) #獲取網頁資料
resp.encoding='utf-8'
while 1 :
    course=BeautifulSoup(resp.text,"html.parser")
    # 以 Beautiful Soup 解析 HTML 程式碼

    usercourse=course.find("td",string=num)

    front=usercourse.find_previous_siblings("td",limit=1)

    back=usercourse.find_next_siblings("td",limit=14)


    for info in front:
        infoarray.append(info.string)
    infoarray.append(num)
    for info in back:
         infoarray.append(info.string)

    balance = back.pop().string

    print("課程資訊: ")

    for info in infoarray:
        if(info!=" "):
            if(infoarray.index(info)==len(infoarray)-1):
                print(info)
            else:
                print(info,end=" | ")

    print("餘額為: "+ balance)

    if(balance=="不限"or balance=="額滿"):
        print("Don't worry ")
        break
    else:
        b=int(balance)
        if(b>0):
            print("搶課去!!!! ---> https://course.ncku.edu.tw/course/signin.php"  )
        else:
            print("明年請早QQQ")
        infoarray.clear()
        sleep(2.0)
     
