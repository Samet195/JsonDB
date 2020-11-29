from JsonDB import JsonDB

db = JsonDB("ExampleDB.json")

print(db.ShowTables())

print(db.GetCols("Users"))

print(db.Select("Users"))

print(db.Select("Users","User"))

input("\n--Enter_to_Continue--")
