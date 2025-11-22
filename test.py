
import modals

import modals.db

import modals
import modals.columns
import modals.db
db = modals.db.DataBase("app")
columns_map = {"id": modals.columns.Column("id", 1, False),"name":modals.columns.Column("name", 2, False),"job":modals.columns.Column("job",2,False),"age":modals.columns.Column("age", 1, False),"is_cool":modals.columns.Column("is_cool", 1, False)} 
columns_list =columns_map.keys()
table = db.create_tables("test", columns_list, columns_map)

record = {'id':1, 'name':"Shreyank", 'job':"randomguy", 'age':3, 'is_cool':4}

table.insert(record)

import time
start = time.time()

table.select()
print(time.time() - start)
