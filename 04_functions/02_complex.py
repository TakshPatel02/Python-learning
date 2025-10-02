# You're creating a monthly report for a cafe's sales. instead of puttinh all logic together in one place , break it down.
#Task: write a function generate_report() that calls : fetch_sales() , filter_valid_orders() , summarize_data().

def fetch_sales():
    print("fetching sales data from database...")

def filter_valid_orders():
    print("filtering valid orders...")

def summarize_data():
    print("summarizing data...")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print("report generated successfully.")

generate_report()

# This modular approach makes the code easier to read and maintain. Each function has a single responsiibility , making debugging and future updates simpler.