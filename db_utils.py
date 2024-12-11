import sqlite3
import os
import fnmatch
from cksum import memcrc

def create_db(db_loc):
    con = sqlite3.connect(db_loc)
    cur = con.cursor()
    cur.execute('CREATE TABLE "item" ("id"	TEXT NOT NULL,"cksum"	INTEGER NOT NULL, "path"	TEXT NOT NULL, PRIMARY KEY("id"))')


def catalog_items(dir, db_loc):
    con = sqlite3.connect(db_loc)
    cur = con.cursor()

    for root, dir, files in os.walk(dir):
        for extension in ['jpg', 'jpeg', 'gif', 'png']:
            for filename in fnmatch.filter(files, '*.' + extension):
                j = os.path.join(root, filename)
                print(root, filename)
                buffer = open(j, 'rb').read()
                ck = memcrc(buffer)
                print(ck)
                data = (filename, ck, root)
                cur.execute("insert into item VALUES (?, ?, ?)", data)
    con.commit()
    con.close()

