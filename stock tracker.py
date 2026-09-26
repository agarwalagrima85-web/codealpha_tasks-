def stock_tracker():
    # 1. Hardcoded dictionary to define stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 175,
        "MSFT": 400
    }
    
    print("Welcome to the Simple Stock Tracker!")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"  - {stock}: ${price}")
        
    total_investment = 0
    portfolio = []
    
    # 2. User inputs stock names and quantity
    while True:
        stock_name = input("\nEnter stock symbol (e.g., AAPL) or type 'done' to finish: ").upper().strip()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print("Stock not found in price list. Please try a valid stock name.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity of shares for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number for quantity.")
            continue
            
        # Calculate investment for this stock
        price = stock_prices[stock_name]
        item_total = price * quantity
        total_investment += item_total
        
        # Save to our portfolio list
        portfolio.append((stock_name, quantity, item_total))
        print(f"Added: {quantity} shares of {stock_name} = ${item_total}")
        
    # 3. Display total investment value
    print("\n" + "="*30)
    print("PORTFOLIO SUMMARY")
    print("="*30)
    for stock, qty, val in portfolio:
        print(f"{qty}x {stock} -> ${val}")
    print("-"*30)
    print(f"Total Investment Value: ${total_investment}")
    print("="*30)
    
    # 4. Optionally save the result in a text file
    save_file = input("\nWould you like to save this result to a text file? (y/n): ").lower().strip()
    if save_file == 'y':
        with open("stock_report.txt", "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            for stock, qty, val in portfolio:
                f.write(f"{qty}x {stock} -> ${val}\n")
            f.write(f"Total Investment Value: ${total_investment}\n")
        print("Results successfully saved to 'stock_report.txt'!")

if __name__ == "__main__":
    stock_tracker()