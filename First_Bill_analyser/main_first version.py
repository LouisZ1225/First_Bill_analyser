import pandas as pd

# 读取账单数据
data = pd.read_csv("Book1.csv")

print("账单数据：")
print(data)

total = data["amount"].sum()

print("总消费：", total)

category_total = data.groupby("category")["amount"].sum()

print("\n分类消费：")
print(category_total)

max_row = data.loc[data["amount"].idxmax()]

print("\n最大消费：")
print(max_row["item"], max_row["amount"])