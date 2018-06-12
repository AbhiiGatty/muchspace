#! /usr/bin/env python3

import fire
from pathlib import Path
from scripts import fastRequests
class MuchSpace:
    """ Fire Class for muchspace Operations 
        Author: abhiigatty 
        Email: abhiigatty@gmail.com\n
            muchspace: The link status checking CLI.
            Example usage:
            muchspace getinfo <FILE_PATH> or
            muchspace getinfo <FILE_PATH> --report # The --report will generate a json report 
            i.e
            muchspace getinfo --file-path <FILE_PATH> [--report]"""

    def __init__(self):
        print("muchspace v2 - Pre-Alpha")

    """ Function to stack the given directory based on extensions"""
    def getinfo(self, file_path, report = False):
        """ muchspace: The link status checking CLI.""" 
        fastRequests.main(file_path=file_path, report=report) # Call main to start processing file_path

def main():
    fire.Fire(MuchSpace)

if __name__ == '__main__':
    main()
















  