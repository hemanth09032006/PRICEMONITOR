import re

def analyze_market_data():
    price_history = {}
    error_count = 0
    total_records = 0

    print("Opening tracking_logs.txt for high-performance analysis...")
    
    with open("tracking_logs.txt", "r") as file:
        for line in file:
            total_records += 1
            if "[ERROR]" in line:
                error_count += 1
                continue
            
            match = re.search(r"Name:(.*?) Price:(\d+)", line)
            if match:
                prod_name = match.group(1)
                price = int(match.group(2))
                
                if prod_name not in price_history:
                    price_history[prod_name] = []
                price_history[prod_name].append(price)

    # Added encoding="utf-8" right here to fix the Windows crash!
    with open("Market_Report.md", "w", encoding="utf-8") as report:
        report.write("# E-Commerce Data Analytics Report\n")
        report.write(f"**Total Logs Processed:** {total_records} | **Network Failures Blocked:** {error_count}\n\n")
        report.write("## Price Metrics Summary\n")
        report.write("| Product Name | Min Price | Max Price | Average Price |\n")
        report.write("| --- | --- | --- | --- |\n")
        
        for prod_name, prices in price_history.items():
            min_p = min(prices)
            max_p = max(prices)
            avg_p = sum(prices) // len(prices)
            report.write(f"| {prod_name} | ₹{min_p} | ₹{max_p} | ₹{avg_p} |\n")
            
    print("Analysis finished! Check your sidebar for 'Market_Report.md'.")

if __name__ == "__main__":
    analyze_market_data()