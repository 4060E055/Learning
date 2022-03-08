from bs4 import BeautifulSoup

with open(r"C:\AIcalss\Python爬蟲\Exercises\table.html", "r", encoding="utf-8") as fp:
    # 建立BeautifulSoup物件並指定檔案輸入物件
    soup = BeautifulSoup(fp, "html.parser")

a = soup.select('tr')
#print("a =\n", a)

q = []
for i in a:
    q.append(i.find_all())

print("q =", q)

n = 0
m = 0
for i in q:
    m = 0
    for j in i:
        q[n][m] = j.text
        m += 1
    n += 1
del q[0]
print("ans =", q)

# --------------------


# # teacher's ans
# with open(r"C:\AIcalss\Python爬蟲\Exercises\table.html", "r", encoding="utf-8") as fp:
#     # 建立BeautifulSoup物件並指定檔案輸入物件
#     soup = BeautifulSoup(fp, "html.parser")
# friends = []
# trs = soup.select('tr')
#
# for i in range(1, len(trs)):
#     tr = trs[i]
#     friend = []
#     for td in tr.select('td'):
#         friend.append(td.text.strip())
#     friends.append(friend)
#
# print(friends)
