import csv

# Load CSV data into a dictionary on startup
product_data = {}

with open("/code/stockinfo.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product_data[row["productID"]] = int(row["stock"])

def get_stock_info(product_id: str):
    if product_id in product_data:
        return {"productID": product_id, "available": product_data[product_id]}
    return None