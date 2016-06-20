#!/usr/bin/python

import os.path

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

if os.path.isfile(options.filename):
    print('loading dup files from {}'.format(options.filename))
else:
    print('file {} doesn\'t exists'.format(options.filename))
    exit(2)

options.filename_keep = options.filename + '.keep'
options.filename_remove = options.filename + '.remove'

fk = open(options.filename_keep, 'w')
fr = open(options.filename_remove, 'w')
list_files = []
chosen = last_one = ''
with open(options.filename, encoding='utf-8') as a_file:
    for a_line in a_file:
        if len(a_line) > 1:
            list_files.append(a_line)
        else:
            while True:
                print('Select files you want to keep in each group.')
                for idx, val in enumerate(list_files):
                    print('{:>5}) {}'.format(idx, val.rstrip()))
                chosen = input('Enter file to keep: ')
                try:
                    if chosen == '':
                        chosen = last_one
                    if len(list_files) > int(chosen):
                        break
                    else:
                        print("Insert integer between 0 and {}".format(len(list_files) - 1))
                except ValueError:
                    print("That's not an int!")
            chosen_int = int(chosen)
            last_one = chosen_int
            for idx, val in enumerate(list_files):
                if int(idx) == chosen_int:
                    fk.write('"' + val.rstrip() + '"\n')
                    print('You choose: {0} - {1}'.format(chosen_int, val.rstrip()))
                else:
                    fr.write('"' + val.rstrip() + '"\n')
            list_files = []
