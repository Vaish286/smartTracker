# Handcoded stock prices
stock_prices = {
    "Apple": 180,
    "Tesla": 258,
    "Google": 140,
    "Microsoft": 320,
    "Amazon": 125
}

# Store portfolio data
portfolio = {}

print("Enter your stock portfolio (type 'done' to finish):")

# Input loop
while True:
    stock = input("Stock Symbol (e.g., Apple, Tesla, Amazon,Google, Microsft ): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to file
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (e.g., portfolio.txt): ")
    with open(filename, 'w') as file:
        file.write("Stock Portfolio:\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"Saved to {filename}")
