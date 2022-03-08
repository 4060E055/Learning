# 變化題 顯示第幾頁到第幾頁內容

import requests

from bs4 import BeautifulSoup


# 抓該頁資料
def get_web_data(_soup):
    for i in _soup.select('div.book-data-inner'):
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


tenlong = "https://www.tenlong.com.tw"
url = tenlong + "/search?availability=buyable&display=list&keyword=python&langs%5B%5D=all"  # python搜尋後的第一頁

# 給予表頭
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/96.0.4664.110 Safari/537.36"}

# page = int(input("要顯示幾頁內容？"))

try:
    page_list = list(map(int, input("要顯示第幾頁到第幾頁的內容？(ex:2到3頁請輸入「2-3」)").strip().split("-")))
    if page_list[0] > page_list[1]:
        print("請輸入小至大的數字")
    elif page_list[0] > 0:
        now_page = 1
        # print(url)  # index web
        while now_page <= page_list[1]:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            if page_list[0] <= now_page <= page_list[1]:
                print("\n第", now_page, "頁內容：")
                get_web_data(soup)  # 取得資料

            page_web = soup.select_one('div.pagination.pagination-footer a.next_page')  # 找出下一頁網址
            # print(tenlong + page_web['href'])
            try:
                url = tenlong + page_web['href']
            except:
                print("沒有下一頁了")
                break

            now_page += 1

except:
    print("請不要亂輸入")
