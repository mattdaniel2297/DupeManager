import os
import sys

# find unique extensions
def test(root_dir):
    extensions = []
    print(root_dir)
    for root, dir, files in os.walk(root_dir):
        for f in files:
            # print(f)
            ext = os.path.splitext(f)[1]
            if ext not in extensions:
                extensions.append(ext)
    print(extensions)


test(sys.argv[1])