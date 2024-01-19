#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
# from models.engine.file_storage import FileStorage
# from models.engine.db_storage import DBStorage
import os


HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")
# storage = DBStorage()
# storage.reload()

if (HBNB_TYPE_STORAGE == "db"):
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
elif (HBNB_TYPE_STORAGE == "FileStorage"):
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
