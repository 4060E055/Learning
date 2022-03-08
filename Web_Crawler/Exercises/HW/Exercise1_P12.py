from bs4 import BeautifulSoup
import re

with open(r"C:\AIcalss\Python爬蟲\Exercises\basic.html", "r", encoding="utf-8") as fp:
    # 建立BeautifulSoup物件並指定檔案輸入物件
    soup = BeautifulSoup(fp, "html.parser")

# 1.1簡單方法　　（不加　</li> 輸出多tap）
print("第一題方法一：", soup.ul.text)

# 1.2其他詳細方法
print("第一題方法二：", soup.find('ul').text.replace("\t", ""))

# # 1.3 teacher's ans ???
# for tag in soup.ul("li"):
#     text = tag.text.strip().replace("\t", "")  # 去除tab
#     print(text)

# 2.1簡單方法
print("第二題方法一：", soup.a['href'])

# 2.2依據關鍵字內容查找方法
ans = soup.find_all('a', string=re.compile('GOOGLE搜尋網站'))
# 因為她是list，所以需要額外用迴圈去搜尋，如果是find只找一個就不用
print(ans)
print("第二題方法二：", ans[0]['href'])


# # 2.3 teacher'ans ???
# for a in soup.find("a",string="GOOGLE搜尋網站"):
#     print(a)
