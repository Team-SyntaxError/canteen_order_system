
from database import db_x

filter = db_x["RECIPE"]
fc_filter = db_x["FC"]
def add_recipe(recipe,stock,price,is_special):
    filter.insert_one(
            {"recipe": recipe, "stock": stock, "price": price,"is_special":is_special}
        )

def remove_recipe(recipe):
    filter.delete_one(
            {"recipe": recipe}
        )

def is_recipe(recipe):
    lol = filter.find_one(
            {"recipe": recipe}
        )
    return lol

def list_recipes():
    cursor = filter.find({})
    return cursor

def update_recipe_stock(receipe_dict):
    receipe=list(receipe_dict.keys())[0]
    filtere = { "recipe": receipe }
    newvalues = { "$set": { "stock": receipe_dict.get(receipe) } }
    filter.update_one(filtere,newvalues)

def update_recipe_price(receipe_dict):
    receipe=list(receipe_dict.keys())[0]
    filtere = { "recipe": receipe }
    newvalues = { "$set": { "price": receipe_dict.get(receipe) } }
    filter.update_one(filtere,newvalues)

def get_tokens():
    return fc_filter.find({})