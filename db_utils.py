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

    total = 0
    count = 0
    for root, dir, files in os.walk(dir):
        for extension in ['jpg', 'jpeg', 'gif', 'png' ,'webp', 'mp4', 'webm', 'avi', 'mov', 'wmv', 'ogg', 'mkv']:
            for filename in fnmatch.filter(files, '*.' + extension):
                j = os.path.join(root, filename)
                print(root, filename)
                buffer = open(j, 'rb').read()
                ck = memcrc(buffer)
                print(ck)
                data = (filename, ck, root)
                cur.execute("insert into item VALUES (?, ?, ?)", data)
                count += 1
                if count > 1000:
                    con.commit()
                    total += count
                    count = 0
                    print(f"----- rows created so far: {total} -----")
    con.commit()
    con.close()
    print(f"total items: {total}")

