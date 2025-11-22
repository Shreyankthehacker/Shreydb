import modals
from pathlib import Path
from configs import constants
import os

import modals.columndefreader
import modals.reader
import modals.recordparser
import modals.tables 

class DataBase:
    name : str 
    path : str
    tables : dict # key is the table name and value is the modals.table object  
    

    def __init__(self,name):
        self.name = name 
        self.path = Path(constants.BaseDir).joinpath(name)
        self.tables = {}
        if self.path.exists():
            print("Path already exists!")
        else:
            os.makedirs(self.path)
            
        self.tables = self.read_tables()
        

    # def create_tables(self,name:str,columns_list,columns_map):
    #     table_path = (self.path / name).with_suffix(constants.Table_FileExtension)

    #     try:
    #         table_path.open("rb").close()
    #         raise FileExistsError("Table name already exists")
    #     except FileNotFoundError:
    #         pass

    #     try:
    #         f = table_path.open("wb")
    #     except Exception as e :
    #         raise KeyError(f"cant create table file {e}")
        
    #     table = modals.tables.Table(file_path=table_path,
    #                                 columnNames=columns_list,
    #                                 columns=columns_map,
    #                             )
    #     recordparser = modals.recordparser.RecordParser(f,columns_list)
    #     table.setRecordParse(recordParser=recordparser)
    #     table.WriteColumnDefinition()
    #     self.tables[name] = table
    #     return table 
    

    # def read_tables(self):
    #     tables = {}

    #     for file in self.path.iterdir():     
    #         if file.name.endswith('_idx') or file.name.endswith('.wal'):
    #             continue

    #         # Fix: Open the file as BufferedReader
    #         # opened_file = file.open('rb')
    #         # r = modals.reader.Reader(opened_file)
    #         t = modals.tables.Table(file_path=str(file))
    #         t.ReadColumnDefinitions()
    #         recordparser = modals.recordparser.RecordParser(file,t.columnNames)
    #         t.setRecordParse(recordParser=recordparser)

    #         tables[t.name] = t

    #     print("total tables in the db are", list(tables.keys()))
    #     return tables
    def create_tables(self, name: str, columns_list, columns_map):
        table_path = str((self.path / name).with_suffix(constants.Table_FileExtension))  # str for open

        p = Path(table_path)
        if p.exists():
            raise FileExistsError("Table name already exists")

        table = modals.tables.Table(file_path=table_path,
                                    columnNames=columns_list,
                                    columns=columns_map)
        recordparser = modals.recordparser.RecordParser(table.file, columns_list)
        table.setRecordParse(recordParser=recordparser)
        table.WriteColumnDefinition()
        self.tables[name] = table
        return table

    def read_tables(self):
        tables = {}
        for file_path in self.path.iterdir():
            if file_path.name.endswith('_idx') or file_path.name.endswith('.wal'):
                continue
            t = modals.tables.Table(file_path=str(file_path))
            t.ReadColumnDefinitions()
            recordparser = modals.recordparser.RecordParser(t.file, t.columnNames)  # t.file, not file_path
            t.setRecordParse(recordParser=recordparser)
            tables[t.name] = t
        print("total tables in the db are", list(tables.keys()))
        return tables

if __name__=='main':
    db = DataBase("db")
    columns_map = {"id": modals.columns.Column("id", 1, False),"name":modals.columns.Column("name", 2, False)} 
    columns_list = ["id","name"]
    table = db.create_tables("mytable", columns_list, columns_map)

