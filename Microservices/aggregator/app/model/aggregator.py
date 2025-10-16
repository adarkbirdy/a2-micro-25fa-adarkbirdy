import requests

ITEM_INFO_URL = "https://iteminfo-image-836478715395.us-west2.run.app/item-info/items/"
STOCK_INFO_URL = "https://stockinfo-image-836478715395.us-west2.run.app/stock-info/items/"

def lookup_product(product_id: str):
    # Query item info
    item_response = requests.get(ITEM_INFO_URL + product_id)
    if item_response.status_code == 404:
        return {"error": "Product not found"}, 404

    item_data = item_response.json()

    # Query stock info
    stock_response = requests.get(STOCK_INFO_URL + product_id)
    if stock_response.status_code == 200:
        stock_data = stock_response.json()
        stock = stock_data.get("available", 0)
    else:
        stock = 0

    return {
        "productID": product_id,
        "name": item_data["name"],
        "available": stock
    }, 200