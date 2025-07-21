import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "AMZN": 3400,
    "NFLX": 520
}

print("\033[1;33m📈💸 Welcome to the Ultimate Stock Portfolio Tracker 💸📈\033[0m")
print("\n\033[1;36m🔥 Available Stocks 🔥\033[0m")
for stock, price in stock_prices.items():
    print(f"\033[1;32m➡️ {stock}: ${price} per share\033[0m")

portfolio = {}
total_investment = 0

print("\n\033[1;35mLet's build your portfolio! Type 'done' when you're finished.\033[0m")

while True:
    stock = input("\n👉 Enter Stock Symbol (AAPL, TSLA, etc.): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("\033[1;31m❌ Invalid stock! Please choose from the available list.\033[0m")
        continue
    try:
        qty = int(input(f"📊 How many shares of {stock}?: "))
        if qty <= 0:
            print("\033[1;31m⚠️ Quantity must be greater than zero!\033[0m")
            continue
        investment = stock_prices[stock] * qty
        portfolio[stock] = portfolio.get(stock, 0) + investment
        total_investment += investment
        print(f"\033[1;32m✅ Added {qty} shares of {stock} worth ${investment}\033[0m")
    except ValueError:
        print("\033[1;31m⚠️ Invalid input! Enter a valid number.\033[0m")

print("\n\033[1;33m=========== 📊 Portfolio Summary 📊 ===========\033[0m")
for stock, investment in portfolio.items():
    print(f"\033[1;36m{stock}: ${investment}\033[0m")
print(f"\n\033[1;32m💵 Total Investment = ${total_investment}\033[0m")

choice = input("\n💾 Do you want to save the report? Type 'txt' or 'csv', or 'no': ").lower()

if choice == 'txt':
    with open("portfolio_summary.txt", "w") as file:
        file.write("📊 Portfolio Summary 📊\n")
        for stock, investment in portfolio.items():
            file.write(f"{stock}: ${investment}\n")
        file.write(f"\nTotal Investment = ${total_investment}\n")
    print("\033[1;32m✅ Portfolio saved in 'portfolio_summary.txt'\033[0m")

elif choice == 'csv':
    with open("portfolio_summary.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Investment ($)"])
        for stock, investment in portfolio.items():
            writer.writerow([stock, investment])
        writer.writerow(["Total", total_investment])
    print("\033[1;32m✅ Portfolio saved in 'portfolio_summary.csv'\033[0m")

else:
    print("\033[1;34m👍 Report not saved. Session ended successfully!\033[0m")
