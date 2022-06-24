from database import db_x

filter = db_x["FC"]

def add(dic, pwd):
    filter.insert_one(
            {"dict": dic, "pwd": pwd, "isvalid":True}
        )
