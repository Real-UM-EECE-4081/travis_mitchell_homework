import os
import collections

def countFileTypes(directory):
    counter = collections.Counter()
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            extension = os.path.splitext(filename)[1]
            counter[extension] += 1
    return counter

print(countFileTypes('venv'))

