# -*- coding: utf-8 -*-

# =============================================================================
# EX4.1 電影和觀眾
# =============================================================================
rank = {'Nick': {'Coco': 1, 'Cold War': 5}, 'John': {'Coco': 5, 'Cold War': 1}}

sortRank=sorted(rank.items(),key=lambda k:k[0])#dict轉list進行姓名排序

for i in range(len(sortRank)):#因為是二維 所以輸出每列的第一項為姓名
    print(sortRank[i][0],end=" ")

print()

sortName=sorted(sortRank[0][1].keys())#針對電影姓名排序

for i in sortName:#輸出電影姓名
        print(i,end=" ")
        
# =============================================================================
# EX4.2 我們的喜好距離
# =============================================================================
import sys
rank = {'Nick': {'Coco': 1, 'Cold War': 5}, 'John': {'Coco': 5, 'Cold War': 1}}
n1 = input().strip()
n2 = input().strip()
rank_sum =0
try:
    for m in rank[n1].keys() :
        rank_sum += (rank[n1][m]-rank[n2][m])**2
        
    import math
    distance = round(math.sqrt(rank_sum),2) #開根號取小數第二位
    print (distance)
except:
    sys.exit()