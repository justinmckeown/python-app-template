import sqlite3
import json 
from typing import Dict, List
#TODO: Import data classes

class Model:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database.db")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.cursor.execute("create table if not exists people (name TEXT, surname TEXT, times_assessed TEXT, date_met TEXT)")