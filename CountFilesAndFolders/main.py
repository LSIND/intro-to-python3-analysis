#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

for root, dirs, files in os.walk('C:\MEGA\EURECA\Python\lab'):
    path = root.split(os.sep)

    count_dirs = count_files = 0
    for f in dirs:
        count_dirs += 1

    for file in files:
        count_files += 1
    print((len(path) - 2) * '--'+'>', os.path.basename(root), ':\t', count_dirs, 'folders, ', count_files, 'files')
