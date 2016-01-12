#!/usr/local/bin/python
import os
import sys

from subprocess import call
start = sys.argv[1]
for root, dirs, files in os.walk(start):
    for file in files:
        if file.endswith('.mobi'):
            epub_path = root + '/' + file.replace('.mobi', '.epub')
            file_path = root + '/' + file
            ret = call(["ebook-convert", file_path, epub_path],
                        stdout=open(os.devnull, 'wb'))
            if ret != 0:
                print("Conversion of " + file + " failed, stopping....")
                exit()

            print(file + " converted successfully")
