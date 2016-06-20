# Little script to handle fdupes output

## Scope
FDUPES produce a file with all duplicate files in a directory, this file is formatted in a specific way
Duplicate files are shown in groups (1 path for each file) separated by an empty line.
Handling this file should be very annoing, so this script in Python 3, help you to divide files to keep and files to remove
FDUPES has his proper method to delete files `-d` option, but I prefer divide in 2 step the work
1. find duplicates
1. get list of files to keep and delete

## What's FDUPES

FDUPES is a program for identifying duplicate files residing
within specified directories. [fdupes repository](https://github.com/adrianlopezroche/fdupes)

## Usage

```:~$ pyton3  dedup.py -f <fdupes.output>```
At the end of process you'll find, in the same directory, a file .keep and a file .remove

