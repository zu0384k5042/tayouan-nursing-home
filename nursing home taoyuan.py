#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
"""
Mac 的使用者　如果出現　SSL Certificate Error
請執行以下的程式，HTTPS 就能工作
/Applications/python 3.6/Install Certificates.command
"""

import json
import sys

import numpy as np
import matplotlib.pyplot as plt


try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x


# print(len(sys.argv))
if len(sys.argv)>1:
    sarea=sys.argv[1]
if len(sys.argv)>2:
    DataType=sys.argv[2]

import ssl
context = ssl._create_unverified_context()

url="https://quality.data.gov.tw/dq_download_json.php?nid=128389&md5_url=eb3530786252eb100ce65132ce0447ad"
req=httplib.Request(url)

reponse = httplib.urlopen(req, context=context)

if reponse.code==200:
    if (sys.version_info > (3, 0)):
        contents = reponse.read().decode("utf-8");
    else:
        contents = reponse.read()
    data = json.loads(contents)
    listtsat = []  # 桃園區地址
    listtloc = []  # 桃園區域
    listtdate = []  # 桃園開業日期
    listtprin = []  # 桃園負責人
    listtopen = []  # 桃園開放床數
    listtphone = []  # 桃園電話

    listgsat = []  # 龜山區地址
    listgloc = []  # 龜山區域
    listgdate = []  # 龜山開業日期
    listgprin = []  # 龜山負責人
    listgopen = []  # 龜山開放床數
    listgphone = []  # 龜山電話

    listcsat = []  # 中壢區地址
    listcloc = []  # 中壢區域
    listcdate = []  # 中壢開業日期
    listcprin = []  # 中壢負責人
    listcopen = []  # 中壢開放床數
    listcphone = []  # 中壢電話

    listpsat = []  # 平鎮區地址
    listploc = []  # 平鎮區域
    listpdate = []  # 平鎮開業日期
    listpprin = []  # 平鎮負責人
    listpopen = []  # 平鎮開放床數
    listpphone = []  # 平鎮電話

    listlsat = []  # 龍潭區地址
    listlloc = []  # 龍潭區域
    listldate = []  # 龍潭開業日期
    listlprin = []  # 龍潭負責人
    listlopen = []  # 龍潭開放床數
    listlphone = []  # 龍潭電話

    listdsat = []  # 大溪區地址
    listdloc = []  # 大溪區域
    listddate = []  # 大溪開業日期
    listdprin = []  # 大溪負責人
    listdopen = []  # 大溪開放床數
    listdphone = []  # 大溪電話

    listbsat = []  # 八德區地址
    listbloc = []  # 八德區域
    listbdate = []  # 八德開業日期
    listbprin = []  # 八德負責人
    listbopen = []  # 八德開放床數
    listbphone = []  # 八德電話

    listisat = []  # 觀音區地址
    listiloc = []  # 觀音區域
    listidate = []  # 觀音開業日期
    listiprin = []  # 觀音負責人
    listiopen = []  # 觀音開放床數
    listiphone = []  # 觀音電話

    listusat = []  # 楊梅區地址
    listuloc = []  # 楊梅區域
    listudate = []  # 楊梅開業日期
    listuprin = []  # 楊梅負責人
    listuopen = []  # 楊梅開放床數
    listuphone = []  # 楊梅電話

    listxsat = []  # 新屋區地址
    listxloc = []  # 新屋區域
    listxdate = []  # 新屋開業日期
    listxprin = []  # 新屋負責人
    listxopen = []  # 新屋開放床數
    listxphone = []  # 新屋電話

    listBIsat = []  # 大園區地址
    listBIloc = []  # 大園區域
    listBIdate = []  # 大園開業日期
    listBIprin = []  # 大園負責人
    listBIopen = []  # 大園開放床數
    listBIphone = []  # 大園電話


def copedatainlist():  #將數據分類複製到

    for data2 in data:
        if data2["區域"] == "桃園區":
            listtsat.append(data2["地址"])
            listtloc.append(data2["區域"])
            listtdate.append(data2["開業日期"])
            listtprin.append(data2["負責護理人員"])
            listtopen.append(data2["開放床數"])
            listtphone.append(data2["電話"])

        if data2["區域"] == "龜山區":
            listgsat.append(data2["地址"])
            listgloc.append(data2["區域"])
            listgdate.append(data2["開業日期"])
            listgprin.append(data2["負責護理人員"])
            listgopen.append(data2["開放床數"])
            listgphone.append(data2["電話"])

        if data2["區域"] == "中壢區":
            listcsat.append(data2["地址"])
            listcloc.append(data2["區域"])
            listcdate.append(data2["開業日期"])
            listcprin.append(data2["負責護理人員"])
            listcopen.append(data2["開放床數"])
            listcphone.append(data2["電話"])

        if data2["區域"] == "平鎮區":
            listpsat.append(data2["地址"])
            listploc.append(data2["區域"])
            listpdate.append(data2["開業日期"])
            listpprin.append(data2["負責護理人員"])
            listpopen.append(data2["開放床數"])
            listpphone.append(data2["電話"])

        if data2["區域"] == "龍潭區":
            listlsat.append(data2["地址"])
            listlloc.append(data2["區域"])
            listldate.append(data2["開業日期"])
            listlprin.append(data2["負責護理人員"])
            listlopen.append(data2["開放床數"])
            listlphone.append(data2["電話"])

        if data2["區域"] == "大溪區":
            listdsat.append(data2["地址"])
            listdloc.append(data2["區域"])
            listddate.append(data2["開業日期"])
            listdprin.append(data2["負責護理人員"])
            listdopen.append(data2["開放床數"])
            listdphone.append(data2["電話"])

        if data2["區域"] == "大園區":
            listBIsat.append(data2["地址"])
            listBIloc.append(data2["區域"])
            listBIdate.append(data2["開業日期"])
            listBIprin.append(data2["負責護理人員"])
            listBIopen.append(data2["開放床數"])
            listBIphone.append(data2["電話"])

        if data2["區域"] == "八德區":
            listbsat.append(data2["地址"])
            listbloc.append(data2["區域"])
            listbdate.append(data2["開業日期"])
            listbprin.append(data2["負責護理人員"])
            listbopen.append(data2["開放床數"])
            listbphone.append(data2["電話"])

        if data2["區域"] == "觀音區":
            listisat.append(data2["地址"])
            listiloc.append(data2["區域"])
            listidate.append(data2["開業日期"])
            listiprin.append(data2["負責護理人員"])
            listiopen.append(data2["開放床數"])
            listiphone.append(data2["電話"])

        if data2["區域"] == "楊梅區":
            listusat.append(data2["地址"])
            listuloc.append(data2["區域"])
            listudate.append(data2["開業日期"])
            listuprin.append(data2["負責護理人員"])
            listuopen.append(data2["開放床數"])
            listuphone.append(data2["電話"])

        if data2["區域"] == "新屋區":
            listxsat.append(str(data2["地址"]))
            listxloc.append(data2["區域"])
            listxdate.append(data2["開業日期"])
            listxprin.append(data2["負責護理人員"])
            listxopen.append(int(data2["開放床數"]))
            listxphone.append(data2["電話"])

copedatainlist()


#畫圖
plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

plt.subplot(3,3,1)
plt.plot(listxsat,listxopen, 'r-', label="需求人數")
plt.title('2015年 景氣樂觀情況下 機械產業類別需求人數')
plt.legend()




plt.show()




