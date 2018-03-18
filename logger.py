import os
import time
import sys

file_name, path_to_watch = sys.argv
before = dict([(f, None) for f in os.listdir(path_to_watch)])

while True:
    time.sleep(10)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]

    if added:
        print(added)

    before = after
