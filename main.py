import argparse
import os
from test import test

parser = argparse.ArgumentParser("DupeManager")
parser.add_argument("dir", help="directory of files to catalog and manage")
args = parser.parse_args()

if os.path.isdir(args.dir):
    root = args.dir
    print(f"Process root {root}")
    test(root)
else:
    raise Exception("Root is not a valid directory")