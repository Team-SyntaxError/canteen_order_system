from database import db_x

filter = db_x["FC"]

def add(dic, key):
    filter.insert_one(
            {"dict": dic, "key": key, "isvalid":True}
        )
        
def delete(key):
  filter.delete_one({"key":key})


def checker(key):
  return filter.find_one({},{"key":key})
