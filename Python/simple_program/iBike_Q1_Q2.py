# -*- coding: utf-8 -*-
"""
1.由北到南印出所有車站、位置、緯度
2.每個區域iBike station 的數量
3.當時車站被借出率最高的前三名(空位數/總停車格)
4.那些車站暫停營業，或是無車可借，或是無位可停
"""

import json
from pprint import pprint


##直接網路上抓資料
#from urllib import request
#
#url = 'json網址'
#
#jdata = request.urlopen(url).read().decode("utf-8")


# =============================================================================
# 讀取json檔資料並轉為python格式
# =============================================================================
file = 'data/臺中市公共自行車_iBike_租借站_即時車位資料.JSON'
with open(file,encoding='UTF-8') as file:
        data = file.read() #讀檔
jdata = json.loads(data) #從json轉python格式

pprint(jdata) #格式化印出

with open('data/iblkeData.txt','w') as f:
    for i in jdata:
        f.write(str(i)+'\n')

# =============================================================================
# 1.由北到南印出所有車站、位置、緯度
# 進行特定資料的抓取(站名、位址、緯度)
# =============================================================================
station = [] #宣告陣列
for st in jdata:#一筆一筆抓資料放到list裡
    name,addr,lat = st['Position'],st['CAddress'],st['Y']#抓出站名、位址、緯度
    item = (name,addr,lat)#集合成一個tuple
    station.append(item)#再新增成一個二維tuple
pprint(station)


# =============================================================================
# 由北到南排序並寫數txt檔
#緯度越小越南端(台灣在上半球)
# =============================================================================
station.sort(key=lambda x:x[2],reverse = True)
pprint(station)
with open('data/ibikeSorted.txt','w') as f:
    for i in station:
        f.write(str(i)+'\n')


# 2.每個區域iBike station 的數量
# =============================================================================
# 計算每個區域ibike station數量
# =============================================================================
area = {}#宣告字典{區域名稱:數量}
for i in jdata:
    address = i['CArea'] #擷取區域名
    if address in list(area.keys()):#判斷是否有這個區域名
        area[address] = area[address] + 1#此區域數量+1
    else:#沒有則新增該key，並設定數量1
         area[address] = 1

# #進行數量小到大排序
#pprint(sorted(area.items(), key=lambda d: d[1]))
         
#印出每站數量
with open('data/iBikeStationCount.txt','w') as f:
    for (key,value) in area.items():
        f.write("{0}:{1}\n".format(key,value))
        
        