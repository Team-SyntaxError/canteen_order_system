
from database import db_x

filter = db_x["FC"]
filter_product = db_x["RECIPE"]
def add(dic, pwd,is_parcel):
    filter.insert_one(
            {"dict": dic, "key": pwd, "isvalid":True, "is_parcel":is_parcel}
        )

def list_recipes():
    cursor = filter_product.find({})
    return cursor

def key_info(key):
    lol = filter.find_one({"key":key})
    if not lol.get("isvalid"):
        return False
    else:
        return lol

def update_recipe_stock(receipe_dict):
    print(receipe_dict)
    for x in receipe_dict:
        print(x)
        print(receipe_dict.get(x))
        filtere = { "recipe": x }
        newvalues = { "$set": { "stock": str(receipe_dict.get(x)) } }
        filter_product.update_one(filtere,newvalues)
