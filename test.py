import sqlite3
import os
from db_utils import create_db, catalog_items


def test(root_dir):
    db_loc = os.path.join(root_dir, "database.db")
    if not os.path.exists(db_loc):
        create_db(db_loc)
    catalog_items(root_dir, db_loc)
        

