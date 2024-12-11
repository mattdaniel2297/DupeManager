import sqlite3
import os
import fnmatch

def create_db(db_loc):
    con = sqlite3.connect(db_loc)
    cur = con.cursor()
    cur.execute('CREATE TABLE "item" ("id"	TEXT NOT NULL,"cksum"	INTEGER NOT NULL, "path"	TEXT NOT NULL, PRIMARY KEY("id"))')


def catalog_items(dir):
    for root, dir, files in os.walk(dir):
        for extension in ['jpg', 'jpeg', 'gif', 'png']:
            for filename in fnmatch.filter(files, '*.' + extension):
                print(filename)