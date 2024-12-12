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


def dedupe(db_loc):
    con = sqlite3.connect(db_loc)
    cur = con.cursor()
    res = cur.execute("""select cksum, count(*)
            from item
            group by cksum
            having count(*) > 1""")
    data = res.fetchall()
    cur.close()

    print(len(data))
    for item in data:
        cur = con.cursor()
        res = cur.execute(f"select * from item where cksum = {item[0]}")
        dupe_data = res.fetchall()
        print(f"dupe_count from data {len(dupe_data)}")
        dupe_count = len(dupe_data)
        for dupe_item in dupe_data[1:]:
            file_to_delete = os.path.join(dupe_item[2], dupe_item[0])
            print(file_to_delete)
            os.remove(file_to_delete)
    cur.close()    
    con.close()