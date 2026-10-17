
import csv
import os
from datetime import datetime

# Predefined stock prices (sample prices, not live market data)
stock_prices = {
    "AAPL": 230.00,
    "GOOGL": 165.00,
    "MSFT": 420.00,
    "TSLA": 250.00,
    "AMZN": 190.00
}

CSV_FILE = "stock_transactions.csv"


def save_to_csv(ticker, price, shares, total_value):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date", "Ticker", "Price",
                "Shares", "Total Value"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ticker, f"{price:.2f}",
            f"{shares:g}", f"{total_value:.2f}"
        ])


def main():
    portfolio = []
    print("\n===== STOCK TRACKER =====")
    print("Available stocks:", ", ".join(stock_prices))

    while True:
        ticker = input(
            "\nEnter stock ticker (or 'done' to finish): "
        ).strip().upper()

        if ticker == "DONE":
            break

        if ticker not in stock_prices:
            print("Invalid ticker. Please try again.")
            continue

        try:
            shares = float(input("Enter shares owned: "))

            if shares <= 0:
                print("Shares must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        price = stock_prices[ticker]
        total_value = price * shares

        portfolio.append({
            "ticker": ticker,
            "price": price,
            "shares": shares,
            "total": total_value
        })

        save_to_csv(ticker, price, shares, total_value)
        print(f"Added {ticker}: ${total_value:,.2f}")

    if not portfolio:
        print("\nNo stocks were added.")
        return

    print("\n" + "=" * 65)
    print("                 FINANCIAL SUMMARY")
    print("=" * 65)
    print(
        f"{'TICKER':<12}{'PRICE':>12}"
        f"{'SHARES':>12}{'TOTAL VALUE':>18}"
    )
    print("-" * 65)

    for stock in portfolio:
        print(
            f"{stock['ticker']:<12}"
            f"${stock['price']:>10,.2f}"
            f"{stock['shares']:>12.2f}"
            f"${stock['total']:>16,.2f}"
        )

    total_portfolio = sum(
        stock["total"] for stock in portfolio
    )

    print("-" * 65)
    print(f"{'PORTFOLIO TOTAL:':<36}"
          f"${total_portfolio:>16,.2f}")
    print("=" * 65)
    print(f"Transactions saved to {CSV_FILE}")


if __name__ == "__main__":
    main()
