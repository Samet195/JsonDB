# JsonDB

**EN** | [TR](README-TR.md) | [ChangeLog](CHANGELOG.md)

"*An alternative to SQLite in JSON Format!*"

>! This project is still under development.

<br />

### Todos:
- [ ] [Adapt SQLite "Select" Command:](https://www.sqlite.org/images/syntax/select-stmt.gif)
  - [x] Select all datas.
  - [x] Select by column.
  - [x] Select by the `where` parameter.
  - [x] Select by column and the `where` parameter.
  - [ ] The `order_by` parameter will be added to the `select` method.
  - [ ] For too big databases, the limit parameter will be added to the select method.

## How to use
Import the Module and init the class:
```Python
from jsondb import JsonDB
db = JsonDB("ExampleDB.json")
```
Show the tables:
```Python
print(db.show_tables())
# ['Users']
```
Get the columns:
```Python
print(db.get_cols("Users"))
# ['ID', 'User', 'Pass']
```
Selecting the data:
```Python
print(db.select("Users"))
# [(0, 'Samet195', 'abc123'), (1, 'root', 'pass'), (2, 'admin', 'pass')]

print(db.select("Users",col="ID"))
# [0, 1, 2]

print(db.select("Users",col="User"))
# ['Samet195', 'root', 'admin']

print(db.select("Users",where={"ID":0}))
# [(0, 'Samet195', 'abc123')]

print(db.select("Users",where={"Pass":"pass"}))
# [(1, 'root', 'pass'), (2, 'admin', 'pass')]

print(db.select("Users",col="User" ,where={"Pass":"pass"}))
# ['root', 'admin']
```
