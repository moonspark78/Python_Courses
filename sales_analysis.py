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
    best_revenue = revenue[max_revenue_index]

    expensive_products = products[prices > 850]
    high_revenue = revenue[revenue > 3000]
    
    return {
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
        "average_price": average_price,
        "best_product": best_product,
        "best_revenue": best_revenue,
        "expensive_products": expensive_products,
        "high_revenue": high_revenue
    }