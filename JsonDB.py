from json import loads, dumps
from os import path

class JsonDB:
  def __init__(self,db):
    if not db:
      raise Exception("Path is empty")

    elif path.exists(db) and path.isfile(db):
      self.DB = loads(open(db,"r+",encoding="utf-8").read())

    elif path.isdir(db):
      raise Exception("Path is a directory")

    else:raise Exception("Path is not found")

  def show_tables(self):
    return self.DB["TableList"]

  def get_cols(self,table):
    return [cols for cols in self.DB["Tables"][table]["Cols"]]

  def select(self,table,col=None,where=None):
    result = []

    if not col and not where:
      for row in self.DB["Tables"][table]["Rows"]:
        result.append(tuple(row))

    elif col and not where:
      col = self.get_cols(table).index(col)
      for row in self.DB["Tables"][table]["Rows"]:
        result.append(row[col])

    elif not col and where:
      cols = self.get_cols(table)

      i = cols.index(list(where.keys())[0])

      for row in self.DB["Tables"][table]["Rows"]:
        if row[i] == list(where.values())[0]:
          result.append(tuple(row))

    elif col and where:
      cols = self.get_cols(table)

      i = cols.index(list(where.keys())[0])
      col = cols.index(col)

      for row in self.DB["Tables"][table]["Rows"]:
        if row[i] == list(where.values())[0]:
          result.append(row[col])

    return result
