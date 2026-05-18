transactions = [
    ("AAPL", "BUY", 100, 150.00, "2023-01-15"),
    ("GOOGL", "BUY", 50, 2800.00, "2023-01-20"),
    ("AAPL", "BUY", 50, 160.00, "2023-02-10"),
    ("MSFT", "BUY", 75, 300.00, "2023-02-15"),
    ("AAPL", "SELL", 75, 170.00, "2023-03-05"),
    ("GOOGL", "SELL", 20, 2900.00, "2023-03-10"),
    ("TSLA", "BUY", 40, 800.00, "2023-03-15"),
    ("MSFT", "SELL", 25, 320.00, "2023-04-01"),
    ("TSLA", "SELL", 15, 750.00, "2023-04-10"),
    ("AAPL", "BUY", 25, 155.00, "2023-04-15")
]

current_prices = {
    "AAPL": 175.00,
    "GOOGL": 2850.00,
    "MSFT": 310.00,
    "TSLA": 780.00
}



portfolio = {}
trading_volume = {}

for stock, trans_type, qty, price, date in transactions:

    if stock not in portfolio:
        portfolio[stock] = {
            "shares": 0,
            "investment": 0,
            "realized_pl": 0
        }

    if stock not in trading_volume:
        trading_volume[stock] = 0

    trading_volume[stock] += qty

    
    if trans_type == "BUY":
        portfolio[stock]["shares"] += qty
        portfolio[stock]["investment"] += qty * price

    elif trans_type == "SELL":

        avg_cost = (
            portfolio[stock]["investment"] /
            (portfolio[stock]["shares"] + qty)
        )

        realized = (price - avg_cost) * qty

        portfolio[stock]["shares"] -= qty
        portfolio[stock]["realized_pl"] += realized



print("Current Portfolio Holdings:\n")

for stock, data in portfolio.items():
    print(f"{stock}: {data['shares']} shares")



print("\nStock Performance Analysis:\n")

performance_summary = {}

total_investment = 0
total_current_value = 0
total_realized = 0
total_unrealized = 0

for stock, data in portfolio.items():

    shares = data["shares"]
    investment = data["investment"]
    realized_pl = data["realized_pl"]

    current_value = shares * current_prices[stock]

    unrealized_pl = current_value - investment

    total_pl = realized_pl + unrealized_pl

    performance_summary[stock] = total_pl

    total_investment += investment
    total_current_value += current_value
    total_realized += realized_pl
    total_unrealized += unrealized_pl

    print(f"{stock}:")
    print(f"- Total Investment: ${investment:.2f}")
    print(f"- Current Value: ${current_value:.2f}")
    print(f"- Realized P&L: ${realized_pl:.2f}")
    print(f"- Unrealized P&L: ${unrealized_pl:.2f}")
    print(f"- Total P&L: ${total_pl:.2f}\n")



best_stock = max(performance_summary, key=performance_summary.get)
worst_stock = min(performance_summary, key=performance_summary.get)

print(f"Best Performing Stock: {best_stock} "
      f"(${performance_summary[best_stock]:.2f})")

print(f"Worst Performing Stock: {worst_stock} "
      f"(${performance_summary[worst_stock]:.2f})")



overall_pl = total_realized + total_unrealized

return_percentage = (overall_pl / total_investment) * 100

print("\nPortfolio Summary:\n")

print(f"Total Investment: ${total_investment:.2f}")
print(f"Current Portfolio Value: ${total_current_value:.2f}")
print(f"Total Realized P&L: ${total_realized:.2f}")
print(f"Total Unrealized P&L: ${total_unrealized:.2f}")
print(f"Overall P&L: ${overall_pl:.2f}")
print(f"Return Percentage: {return_percentage:.2f}%")


print("\nTrading Volume (Total Shares Traded):\n")

for stock, volume in trading_volume.items():
    print(f"{stock}: {volume} shares")