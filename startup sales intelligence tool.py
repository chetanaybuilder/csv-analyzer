import pandas as pd
data = pd.read_csv("sales.csv.txt")
data["Revenue"] = data["Price"] * data["Quantity"]
best_product = data.loc[data["Revenue"].idxmax()]
worst_product = data.loc[data["Revenue"].idxmin()]
print("total revenue")
total_revenue = (data["Revenue"].sum())
print(total_revenue)
print("best product")
print(best_product)
print("worst product")
print(worst_product)
print("----------------------------startup sales intelligent tool-----------------------------")
top_3_products = data.sort_values("Revenue", ascending=False).head(3)
print("top 3 best products")
print(top_3_products)
average_revenue = data["Revenue"].mean()
print("average Revenue")
print(average_revenue)



