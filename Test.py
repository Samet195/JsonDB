from JsonDB import JsonDB

db = JsonDB("ExampleDB.json")

print(db.showTables())

print(db.getCols("Users"))

print(db.select("Users"))

print(db.select("Users",col="ID"))

print(db.select("Users",col="User"))

print(db.select("Users",where={"ID":0}))

print(db.select("Users",where={"Pass":"pass"}))

input("\n--Enter_to_Continue--")
