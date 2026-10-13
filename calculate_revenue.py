import numpy as np

prices = np.array([1500, 900, 600, 1800, 250, 1000])
quantities = np.array([2, 5, 3, 1, 8, 2])
products = np.array(["MacBook", "iPhone", "iPad", "MacBook", "AirPods", "iPhone"])


def calculate_revenue(prices, quantities):
    return prices * quantities



def analyze_sales(products, prices, quantities):
    revenue = calculate_revenue(prices, quantities)