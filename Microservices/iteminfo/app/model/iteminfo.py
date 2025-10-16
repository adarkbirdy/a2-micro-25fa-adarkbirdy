import csv

# Load CSV data into a dictionary on startup
product_data = {}

with open("/code/iteminfo.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product_data[row["productID"]] = row["name"]

def get_item_info(product_id: str):
    if product_id in product_data:
        return {"productID": product_id, "name": product_data[product_id]}
    return None