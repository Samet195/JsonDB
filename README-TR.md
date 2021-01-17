# JsonDB

[EN](../../) | **TR** | [ChangeLog](CHANGELOG.md)

"*SQLite'ta, JSON Formatında bir Alternatif!*"

>! Bu proje hala geliştirme aşamasındadır.

<br />

### Yapılacaklar:
- [ ] [SQLite "Select" Komutunu Uyarla:](https://www.sqlite.org/images/syntax/select-stmt.gif)
  - [x] Tüm verileri seç.
  - [x] Sütuna göre seç.
  - [x] `where` Parametresine göre seç.
  - [x] Sütuna ve `where` parametresine göre seç.
  - [ ] `select` metoduna `order_by` parametresi eklenecek.
  - [ ] Çok büyük veritabanları için `select` metoduna `limit` parametresi eklenecek.

## Nasıl kullanılır
Modülü içe aktarın ve sınıfı başlatın:
```Python
from jsondb import JsonDB
db = JsonDB("ExampleDB.json")
```
Tabloları göster:
```Python
print(db.show_tables())
# ['Users']
```
Sütunları alın:
```Python
print(db.get_cols("Users"))
# ['ID', 'User', 'Pass']
```
Verilerin seçilmesi:
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
