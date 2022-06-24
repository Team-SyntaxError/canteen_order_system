from database import db_x

filter = db_x["FC"]

def add(dic, key):
    filter.insert_one(
            {"dict": dic, "key": key, "isvalid":True}
        )
        
def delete(key):
  myQuery ={"key":key}
  filter.delete_one(myQuery)

