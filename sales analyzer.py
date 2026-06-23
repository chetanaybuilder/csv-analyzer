import pandas as pd
data = pd.read_csv("sales.csv.txt")
data["Total"] = data["Price"] * data["Quantity"]
best_product = data.loc[data["Total"].idxmax()]
print(data["Total"])
print("the best product")
print(best_product["Product"])
print("total revenue:")
print(data["Total"].sum())