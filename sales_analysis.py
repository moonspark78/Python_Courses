import numpy as np

products = np.array(["MacBook", "iPhone", "iPad", "MacBook", "AirPods", "iPhone"])
prices = np.array([1500, 900, 600, 1800, 250, 1000])
quantities = np.array([2, 5, 3, 1, 8, 2])

def analyze_sales(products, prices, quantities):
    revenue = prices * quantities
    
    total_revenue = revenue.sum()
    total_quantity = quantities.sum()
    average_price = prices.mean()
    
    max_revenue_index = revenue.argmax()
    best_product = products[max_revenue_index]