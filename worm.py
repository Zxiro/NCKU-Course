import requests #python提供的發送http請求的模組
from bs4 import BeautifulSoup #bs4為module名稱 Beautiful...為functionname
infoarray=[]
url = "http://course-query.acad.ncku.edu.tw/qry/"
resp = requests.get(url) #獲取網頁資料
resp.encoding='utf-8'
if resp.status_code==requests.codes.ok: #確定連接成功
    course=BeautifulSoup(resp.text,"html.parser")
# 以 Beautiful Soup 解析 HTML 程式碼
#print(course.prettify())

pro=input('請輸入系所代碼:' )
print(pro)
num=input('請輸入課程代號:')
print(num)

tags=course.find_all("a",href="qry001.php?dept_no="+pro) #找一個option 他的value是 E2
print(tags)
ee="qry001.php?dept_no="+pro
eeurl=url + ee
resp = requests.get(eeurl) #獲取網頁資料
resp.encoding='utf-8'
if resp.status_code==requests.codes.ok: #確定連接成功
    eecourse=BeautifulSoup(resp.text,"html.parser")
usercourse=eecourse.find("td",string=num)
print(usercourse)
front=usercourse.find_previous_siblings("td",limit=1)
back=usercourse.find_next_siblings("td",limit=14)
for info in front:
    infoarray.append(info.string)
infoarray.append(num)
for info in back:
    #print(word.string)
    infoarray.append(info.string)
for info in infoarray:
    if(info!=" "):
        if(infoarray.index(info)==len(infoarray)-1):

            print(info)
        else:
            print(info,end=" | ")
        
   