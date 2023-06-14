import json

with open("catalog.json", "r") as f:
    data = json.load(f)

jacket_count = 0
jacket_max_price = 0
jacket_min_price = float("inf")

for item in data:
    if item["name"] == "jacket":
        jacket_count += 1
        if item["price"] > jacket_max_price:
            jacket_max_price = item["price"]
        if item["price"] < jacket_min_price:
            jacket_min_price = item["price"]

print("ジャケットの個数：", jacket_count)
print("ジャケットの最高価格：", jacket_max_price)
print("ジャケットの最低価格：", jacket_min_price)
