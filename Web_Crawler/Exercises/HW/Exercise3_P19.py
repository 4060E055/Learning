# import requests
#
# from bs4 import BeautifulSoup
#
# url = "https://www.tenlong.com.tw/search?availability=buyable&display=list&keyword=python&langs%5B%5D=all"
# #給予表頭
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
#
# response = requests.get(url, headers=headers)
#
# soup = BeautifulSoup(response.text, "html.parser")
#
# # 測試查找一筆狀況
# # print(soup.select('span.price')[0].text) #售價
# # print(soup.select('span.publish-date')[0].text)#出版日期
# # print(soup.select('strong > a')[0].text)#書名
#
#
# # 查找結果回傳list給變數
# price = soup.select('span.price')
# data = soup.select('span.publish-date')
# name = soup.select('strong > a')
#
# for i in range(len(price)):  # 逐行輸出並且去除空白
#     print(price[i].text.strip(), data[i].text.strip(), name[i].text.strip())


# --------------------------------------
# teacher's 改寫 避免有一本書沒有售價或者日期

import requests

from bs4 import BeautifulSoup

url = "https://www.tenlong.com.tw/search?availability=buyable&display=list&keyword=python&langs%5B%5D=all"
# 給予表頭
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/96.0.4664.110 Safari/537.36"}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

for i in soup.select('div.book-data-inner'):
    name = i.a  # 書名
    data = i.select_one('span.publish-date')  # 出版日期
    price = i.select_one('span.price')  # 價錢
    book = [price, data, name]

    for j in book:
        if j is not None:  # 需先判斷是否有找到標籤
            if j.text.strip() != "":  # 在標籤下是否有text
                print(j.text.strip(), end="\t")  # 才能開始列印資料
            else:
                print("--No Data.--", end="\t")  # 否則回傳無資料
        else:
            print("--No Tag.--", end="\t")  # 否則回傳無資料
    print()
