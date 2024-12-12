import argparse
import os
from db_utils import catalog_items, create_db, dedupe

parser = argparse.ArgumentParser("DupeManager")
parser.add_argument("dir", help="directory of files to catalog and manage")
args = parser.parse_args()


def app(root_dir):
    db_loc = os.path.join(root_dir, "database.db")
    if not os.path.exists(db_loc):
        create_db(db_loc)
        catalog_items(root_dir, db_loc)
        
    dedupe(db_loc)

if os.path.isdir(args.dir):
    root = args.dir
    app(root)
else:
    raise Exception("Root is not a valid directory")
