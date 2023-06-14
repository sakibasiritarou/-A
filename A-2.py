import json

# ファイルの読み込み
with open('catalog.json', 'r') as file:
    data = json.load(file)
    Jcount=0
    jprice=[]

    for d in data:
        if d['name']=='jacket':
            Jcount=Jcount+1
            jprice.append(d['price'])
max_price=max(jprice)
min_price =min(jprice)
            
print("個数",Jcount)
print("最大値",max_price)
print("最小値",min_price)

