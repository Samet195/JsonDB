# JsonDB

EN | [TR](README-TR.md) | [ChangeLog](CHANGELOG.md)

"*An alternative to SQLite in JSON Format!*"

> This project is still under development.

<br />

Todos:
- [ ] [Adapt SQLite "Select" Command:](https://www.sqlite.org/images/syntax/select-stmt.gif)
  - [x] Select all datas.
  - [x] Select by column.
  - [x] Select by the `where` parameter.
  - [ ] Select by column and the `where` parameter.

## How to use
Import the Module and init the class:
```Python
from JsonDB import JsonDB
db = JsonDB("ExampleDB.json")
```
Show the tables:
```Python
print(db.show_tables())
```
Get the columns:
```Python
print(db.get_cols("Users"))
```
