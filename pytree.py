#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Worked together with Mario Rial, Kuljot Anand

import sys

from os import listdir
from os.path import basename, isdir


path_notation = ""
directory_total = 0
file_total = 0


# Main function to print directory tree
def print_directory(root, depth=0, last=False, parent=0):
    directory_count = 0
    file_count = 0
    elements = listdir(root)
    elements.sort()
    
    if(depth == 0):
        if(root[-1] == '/'):
            root = root[:-1]
        print(root)
    else:
        directory_count += 1

        if(last):
            print(("    " * (parent - 1)) + ("│   " * (depth - parent - 1)) + '└── ' + basename(root))
        else:
            print(("    " * (parent)) + ("│   " * (depth - parent - 1)) + '├── ' + basename(root))

    for i, element in enumerate(elements):
        element = root + '/' + element
        
        if (i == len(elements) - 1):
            is_last = True
            if(isdir(element)):
                parent = depth + 1
        else:
            is_last = False

        if(isdir(element)):
            (a, b) = print_directory(element, depth + 1, is_last, parent)
            directory_count += a
            file_count += b
        else:
            print_file(element, depth, is_last, parent)
            file_count += 1

    return (directory_count, file_count)

# Printing and formatting of files in tree structure
def print_file(filename, depth, last=False, previous_depth=0):
    
    spacing = ("    " * previous_depth) + ('│   ' * (depth - previous_depth))

    if(last):
        indent = spacing + '└── '
    else:
        indent = spacing + '├── '
    
    print(indent + basename(filename))

# Set correct path as argument in main function and execute
if __name__ == '__main__':
    if(len(sys.argv) > 1):
        path_notation = sys.argv[1]
    else:
        path_notation = '.'
    (directory_total, file_total) = print_directory(path_notation)
    print()
    print(str(directory_total) + " directories, " + str(file_total) + " files")