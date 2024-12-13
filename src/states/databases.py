import os
from typing import Optional

from constants.path import PathConstants


class DatabasesState:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabasesState, cls).__new__(cls, *args, **kwargs)
            
        return cls._instance
    
    def __init__(self):
        self.dbs: list[str] = os.listdir(PathConstants().DATABASES_PATH)
        self.selected_db: Optional[str] = None
