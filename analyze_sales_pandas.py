import pandas as pd

df = pd.DataFrame({
    
    "product": ["MacBook", "iPhone", "iPad", "MacBook", "AirPods", "iPhone"],
     "price": [1500, 900, 600, 1800, 250, 1000],
     "quantity": [2, 5, 3, 1, 8, 2]
})


def analyze_sales(df):
    df["revenue"] = df["price"] * df["quantity"]
    
    return {
        "total_revenue": df["revenue"].sum(),
        "total_quantity": df["quantity"].sum(),
        "average_price": df["price"].mean(),
         "best_product": df.loc[df["revenue"].idxmax(), "product"],
         "best_revenue": df["revenue"].max(),
         "expensive_products": df.loc[df["price"] > 850, "product"].values,
         "high_revenue": df.loc[df["revenue"] > 3000, "revenue"].values
    }