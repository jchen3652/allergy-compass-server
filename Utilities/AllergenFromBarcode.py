# Standalone assistant to search for products
import openfoodfacts

def getAllergyInfo(barcode):
    toReturn = ""
    raw = openfoodfacts.get_product(barcode) # produces a json
    print(raw)
    text = raw["product"]["allergens_hierarchy"]
    for categories in [["en:peanuts"], ["en:milk"], ["en:molluscs", "en:crustaceans"], ["en:soybeans"]]:
        contains = False
        for test in categories:
            if(test in text):
                contains = True

        toReturn = toReturn + str(int(contains))
        
        
    return toReturn
        
print(getAllergyInfo("20150624"))
    



