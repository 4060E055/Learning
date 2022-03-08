# #---P145 9*9---
# for i in range(1,9+1):
#     for j in range(1,9+1):
#         print(j,"*",i,"=",j*i,end="\t")
#     print()

# #---P146---

# TF = True
# while TF:
#     cm = float(input("請輸入身高(cm)："))
#     kg = float(input("請輸入體重(kg)："))
#     print("您的身高為：", cm, "(cm)\t體重為：", kg, "(kg)")
#     BMI = kg / (cm * 0.01) ** 2
#     print("BMI值為：%.2f" % BMI)  # 體重(公斤)/身高^2(公尺^2)
#
#     if BMI < 18.5:
#         print("診斷結果為：體重過瘦")
#     elif 18.5 <= BMI < 24:
#         print("診斷結果為：標準體重")
#     elif 24 <= BMI < 27:
#         print("診斷結果為：體重過重")
#     elif 27 <= BMI < 30:
#         print("診斷結果為：輕度肥胖")
#     elif 30 <= BMI < 35:
#         print("診斷結果為：中度肥胖")
#     elif 35 <= BMI:
#         print("診斷結果為：重度肥胖")
#
#     while True:
#         key_No = input("請輸入執行代碼：(1.繼續 , 2.停止)：")
#         if key_No == "2":
#             TF = False
#             break
#         elif key_No == "1":
#             break
#         else:
#             print("請不要亂輸入，請再輸入一次！")

# -------P167 del value-------
# score=[98,99,87,78,56,78,78]
# rm=int(input("請輸入要刪除的值："))
# while True:
#     if rm in score:
#         score.remove(rm)
#     else:
#         break
# print("刪除後的score資料：",score)

# ------------P266------------
# list串列：有順序(索引值)、可重複、可修改
# tuple元組：有順序(索引值)、可重複、不可修改
# dictionary字典：key不可重複、value可重複無順序、可修改
# set集合：無順序、無重複、可修改


# ------------P326-------------
# 請問要做出費事數列第幾項?

# 作法一 遞迴
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# n=int(input("請問要做到費事數列第幾項?"))
# for i in range(1,n+1):
#     print(fibonacci(i),end=",")


# 作法二 非遞迴

# n=int(input("請問要做到費事數列第幾項?"))
# fibonacci_2=[0,1]
#
# if n == 0 :
#     print(0)
# elif n>0:
#     print(1, end=",")
#     for i in range(1,n):
#         print(fibonacci_2[i-1]+fibonacci_2[i],end=",")
#         fibonacci_2.append(fibonacci_2[i-1]+fibonacci_2[i])
# else:
#     print("!!請輸入大於0的正整數!!")


# ------------P333~P335--------------
# 把BMI方法寫成函數

# def BMI(cm,kg):
#     print("您的身高為：", cm, "(cm)\t體重為：", kg, "(kg)")
#     BMI = kg / (cm * 0.01) ** 2
#     print("BMI值為：" , BMI)  # 體重(公斤)/身高^2(公尺^2)
#     return BMI
#
#
# def judge(BMI):
#     if BMI < 18.5:
#             print("診斷結果為：體重過瘦")
#     elif 18.5 <= BMI < 24:
#         print("診斷結果為：體重標準")
#     elif 24 <= BMI < 27:
#         print("診斷結果為：體重過重")
#     elif 27 <= BMI < 30:
#         print("診斷結果為：輕度肥胖")
#     elif 30 <= BMI < 35:
#         print("診斷結果為：中度肥胖")
#     elif 35 <= BMI:
#         print("診斷結果為：重度肥胖")
#
#
# cm = float(input("請輸入身高(cm)："))
# kg = float(input("請輸入體重(kg)："))
# yourBMI=BMI(cm,kg)
# judge(yourBMI)


# -------------P449---------------

# # write data in file
#
# data = [['coffee', 100], ['tea', 80], ['juice', 80], ['milk', 70],
#         ['water', 60], ['milktea', 110], ['cake', 60], ['oolong', 50]]
#
# with open("file_name_XXX.txt", 'w+') as file_name:
#     for i in range(len(data)):
#         file_name.write(data[i][0] + "\t" + str(data[i][1]) + "\n")  # write一定要轉換成字串寫入
#
# #----以下作業正式內容 read and process file's
# tt = ""
# # read file and process its
# with open("file_name_XXX.txt", 'r') as file_read:
#     for i in file_read.readlines():
#         a = i.replace("\n", "").split("\t")
#         tt = tt + a[0] + "\t" + a[1] + "\t" + str(float(a[1]) * 0.9) + "\n"
#
#     with open("file_name_YYY.txt", "w") as file_write:
#         file_write.write(tt)
# #-----

# -----------------P463---------------------
# import json
#
# #create file and write data
# data = { "drink":[{"hot":{"coffee":100,"tea":90}},
#                 {"juice":{"apple":95,"banana":85}}],
#         "table":["","A01","A02","A03","A04","A05"]}
#
# with open("file_name_JJJ.json","w+") as file_name:
#     json.dump(data,file_name,indent=4)#write data
#
# #-----以下作業正式
# with open("file_name_JJJ.json","r") as file_name:
#     data=json.load(file_name)#read file
#
# with open("file_name_JJJ.json", "w") as file_name:
#     # print(data["drink"][0]["hot"]["coffee"])
#     data["drink"][0]["hot"]["coffee"] = 90
#     #print(json.dumps(data, indent=4))  # 用於格式化輸出json 輸出型態 string
#     json.dump(data,file_name,indent=4)


# --------------------P581----------------------------
#
# a = int(input("Please enter a number:"))
# s = "{0:^" + str(a * 2) + "}"
# for i in range(1, a * 2, 2):
#     print(s.format("*" * i))

# -------------------P582-----------------------------

# performance = {"name_01": "A", "name_02": "B", "name_03": "C", "name_04": "C",
#                "name_05": "B", "name_06": "A", "name_07": "B", "name_08": "C",
#                "name_09": "C", "name_10": "A", "name_11": "A", "name_12": "B"}
# class_A = {}
# class_B = {}
# class_C = {}
# for key, value in performance.items():
#     if performance[key] == "A":
#         class_A[key] = "A"
#     elif performance[key] == "B":
#         class_B[key] = "B"
#     elif performance[key] == "C":
#         class_C[key] = "C"
#
# print("class_A:", class_A)
# print("class_B:", class_B)
# print("class_C:", class_C)

# ----------------P583-------------------------

# data = (31, 21, 54, 41, 62, 55, 18, 63)
# print("原始資料:", data)
# a = []  # 奇
# b = []  # 偶
# for i in data:
#     if i % 2 == 1:
#         a.append(i)
#     else:
#         b.append(i)
#
# print("odd_list:", a)
# print("even_list:", b)
