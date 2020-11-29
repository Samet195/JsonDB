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
    for col0 in self.DB["Tables"][table]["Cols"]:
      cols.append(col0["Name"])
    return cols

  def Select(self,table,col=None,where=None):
    result = []

    if col == None and where == None:
      for row in self.DB["Tables"][table]["Rows"]:
        result.append(row)

    elif col != None and where == None:
      col = self.GetCols(table).index(col)
      for row in self.DB["Tables"][table]["Rows"]:
        result.append(row[col])

    #elif col == None and where != None:
    #col = self.DB["Tables"][table]["cols"].index(col)
      #for row in self.DB["Tables"][table]["rows"]:
        #result.append(row[col])

    return result
