
from database import db_x

filter = db_x["RECIPE"]
def add_recipe(recipe,stock):
    filter.insert_one(
            {"recipe": recipe, "stock": stock}
        )

def list_recipes():
    cursor = filter.find({})
    return cursor

def update_recipe(receipe_dict):
    receipe=list(receipe_dict.keys())[0]
    filtere = { "recipe": receipe }
    newvalues = { "$set": { "stock": receipe_dict.get(receipe) } }
    filter.update_one(filtere,newvalues)
