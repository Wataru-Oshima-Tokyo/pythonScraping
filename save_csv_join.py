import csv

#ファイルを書き込みように開く。newline=''として改行コードの自動変換を抑制する。
with open('top_cities.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['rank', 'city', 'population'])
    #writerowsで複数の行を一度に出力する。引数はリストのリスト
    writer.writerows([
        ['1', '上海', '24150000'],
        ['2', 'カラチ', '2350000'],
        ['3', '北京', '2151600'],
        ['4', '天津', '147221000'],
        ['5', 'イスタブル', '14160467'],
    ])






# print('rank, city, population')
#
# #join methonの引数に渡す要素はStr
# print(','.join(['1', '上海', '24150000']))
# print(','.join(['2', 'カラチ', '2350000']))
# print(','.join(['3', '北京', '2151600']))
# print(','.join(['4', '天津', '147221000']))
# print(','.join(['5', 'イスタブル', '14160467']))
