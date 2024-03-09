#企業名のリストが必要(5000OpenWork.csv内のタイトルのみ抽出)
#400件くらいで制限が来る
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import urllib
from collections import defaultdict
import html

#########ここのみいじる#############################
"""
準備すべきもの： 
1．headerの名前に「タイトル」が付いた企業名一覧のcsvファイ
2．このファイルを実行するライブラリのダウンロード
startからendまでのindex(表の番号)にある企業データ名の検索をすべてURL化し,電話番号を探します.
check_rangeは、電話番号が見つかったとき、電話番号の前に書いてある情報を指定の文字数分抜き出し、後半の文字をその半分取り出します.(html文字換算のため注意)
pd.read_csv("ファイル名”)　(例)df = pd.read_csv("5000OpenWork.csv")
startからendの範囲は400件以内にする必要があります.

出力形式： result.csv
構成：企業名・URL・電話番号・電話番号前の情報(有益になりそうなのに絞っています・ない場合もあり)
"""
start = 0 #はじめの会社の場所
end = 100 #終わりの会社の場所
check_range = 40
df = pd.read_csv("5000OpenWork.csv")
########いじるの終了##################################

title = df["タイトル"] + " 電話番号"

#企業名から企業の電話番号を調べたURLをまとめてはる

link = []
names = []
#print(title[:10])
for i in range(start,end):
    name = title[i]
    print(name)
    url = 'https://www.google.com/search?q=' + urllib.parse.quote(title[i])
    link.append(url)
    names.append(df["タイトル"][i])

columns = ["企業名","URL"]
df_result = pd.DataFrame(list(zip(names,link)), columns=columns)

#電話番号の取得
#実行時間が長くかかるので注意かつ制限がかかる可能性大
#startとendの値を調整して細かく動作させるとよい
numbers_data = []
numbers_only = []
url = df_result["URL"]
for i in range(end-start):
    lis = []
    lis_number = defaultdict(int)
    r = url[i]
    res = requests.get(r)
    res.encoding = res.apparent_encoding
    S = html.unescape(res.text)
    S = re.sub(re.compile("<.*?>"),"",S)
    S = re.sub(re.compile("{.*?}"),"",S)
    if not re.match(".*[a-z\s\.\,]+",df_result["企業名"][i]):
        S = re.sub(re.compile("[a-z]"),"",S)
    S = S.replace(".","")
    S = S.replace("\xa0","")
    #print(S) 
    elements = re.finditer("\d{2,4}-\d{2,4}-\d{4}",S)
    for element in elements:
        left,right = element.span()
        text = S[left-check_range:right+check_range//2]
        check_name = ["本社電話番号",df_result["企業名"][i]]
        for c_name in check_name:
            if re.search(c_name,text):
                lis.append(text + "|||")
                break
        lis_number[S[left:right]] += 1
    n = list(sorted(lis_number.items(), key=lambda x: x[1],reverse=True))
    numbers_data.append(lis)
    numbers_only.append(n)

df_result["電話番号"] = numbers_only
df_result["電話番号と周辺情報"] = numbers_data
df_result.to_csv("result.csv")
