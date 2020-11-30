from JsonDB import JsonDB

db = JsonDB("ExampleDB.json")

print(db.ShowTables())

print(db.GetCols("Users"))

print(db.Select("Users"))

print(db.Select("Users",col="User"))

print(db.Select("Users",where={"ID":0}))

input("\n--Enter_to_Continue--")
