
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
