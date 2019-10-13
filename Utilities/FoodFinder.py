# Standalone assistant to search for products
import openfoodfacts
import json

while True:
    searchTerm = input("Enter your food query: ")

    raw = openfoodfacts.products.search(searchTerm) # produces a json

    for entry in raw["products"]:
      #  print(entry)
        print(entry["product_name"])
        print(entry["code"])
        print(entry["allergens_hierarchy"])
        print(entry["url"])
        print("\n")
    
