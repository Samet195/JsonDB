from json import loads, dumps
from os import path

class JsonDB:
  def __init__(self,db):
    if path.exists(db) and path.isfile(db):
      self.DB = loads(open(db,"r+",encoding="utf-8").read())

  def ShowTables(self):
    return self.DB["TableList"]

  def GetCols(self,table):
    cols=[]
    for col in self.DB["Tables"][table]["Cols"]:
      cols.append(col)
    return cols

  def Select(self,table,col=None,where=None):
    result = []

    if col == None and where == None:
      for row in self.DB["Tables"][table]["Rows"]:
        result.append(tuple(row))

    elif col != None and where == None:
      pre_result = []
      col = self.GetCols(table).index(col)
      for row in self.DB["Tables"][table]["Rows"]:
        pre_result.append(row[col])
      
      result.append(tuple(pre_result))

    elif col == None and where != None:
      cols = []; rows = []
      for col in self.DB["Tables"][table]["Cols"]:
        cols.append(col)

      i = cols.index(list(where.keys())[0])

      for row in self.DB["Tables"][table]["Rows"]:
        if row[i] == list(where.values())[0]:
          result.append(tuple(row))

    return result
