# -*- coding: utf-8 -*-
"""
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

# =============================================================================
# 3.當時車站被借出率最高的前三名(空位數/總停車格)
# =============================================================================
station = [] #宣告陣列
for st in jdata:#一筆一筆抓資料放到list裡
    #抓出站名、總停車格、空位數
    name,CNT,EmpCNT = st['Position'],int(st['AvailableCNT'])+int(st['EmpCNT']),st['EmpCNT']
    item = (name,float(EmpCNT)/float(CNT)*100)#集合成一個tuple(站名,借出率) 乘100是為了輸出時百分比顯示
    station.append(item)#再新增成一個二維tuple


station.sort(key=lambda k: k[1],reverse=True)#借出率大到小排序
pprint(station)

for st in range(3):
    print("{0}:{1:2.1f}%".format(station[st][0],station[st][1]))
    
# =============================================================================
# 4.那些車站暫停營業，或是無車可借，或是無位可停
# =============================================================================

#新資料沒有顯示暫停營業的站點
#由於剛剛計算借出率，未發現100% or 0%的狀況，故無"無車可借，或是無位可停"的狀況
#結論:此題不用解

