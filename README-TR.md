# JsonDB

[EN](../../) | TR | [ChangeLog](CHANGELOG.md)

"*SQLite'ta, JSON Formatında bir Alternatif!*"

> Bu proje hala geliştirme aşamasındadır.

<br />

### Yapılacaklar:
- [ ] [SQLite "Select" Komutunu Uyarla:](https://www.sqlite.org/images/syntax/select-stmt.gif)
  - [x] Tüm verileri seç.
  - [x] Sütuna göre seç.
  - [x] `where` Parametresine göre seç.
  - [ ] Sütuna ve `where` parametresine göre seç.

## Nasıl kullanılır
Modülü içe aktarın ve sınıfı başlatın:
```Python
from JsonDB import JsonDB
db = JsonDB("ExampleDB.json")
```
Tabloları göster:
```Python
print(db.show_tables())
```
Sütunları alın:
```Python
print(db.get_cols("Users"))
```
Verilerin seçilmesi:
```Python
print(db.select("Users"))

print(db.select("Users",col="ID"))

print(db.select("Users",col="User"))

print(db.select("Users",where={"ID":0}))

print(db.select("Users",where={"Pass":"pass"}))
```
