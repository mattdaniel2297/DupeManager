import sqlite3
import os
from db_utils import create_db, catalog_items


def test(root_dir):
    db_loc = os.path.join(root_dir, "database.db")
    if os.path.exists(db_loc):
        print("database exists")
        catalog_items(root_dir)
    else:
        create_db(db_loc)
    # print(db_loc)
        

