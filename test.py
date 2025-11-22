
import modals

import modals.db

db = modals.db.DataBase("app")
table = db.tables['test']

record = {'id':1, 'name':"Shreyank", 'job':"randomguy", 'age':3, 'is_cool':4}

import time
start = time.time()

table.select()
print(time.time() - start)
