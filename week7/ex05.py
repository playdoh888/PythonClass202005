"""
1) Argparse, is a built in function (I'll google more information on this.)

Correct. Argparse is a standard Python package that helps building a complicate command line "interface".
Re: Pass in the command line parameters, accepting/validating them. It also provide a "standard" help system

2) import the os/sys is defining the environment for running code?

This is actually my bad. I had copied/pasted from the class exercise. It is not needed here.

3) Create the ArgumentParser

        description - Text to display before the argument help (default: none)

3) Create my parser using (This is specific to the item being parsed)

        with tail_filename being the name of the argument or object?

        type - The type to which the command-line argument should be converted.
        help - A brief description of what the argument does.
        metavar - A name for the argument in usage messages.

All correct!

4) args - is this the definition for the method? or is this the command_line stmt that executes my_parser?

        i) my_parser.parse_args() - Is this where the argument described above gets executed?
        ii) is the parse_args() the details described in the my_parser.add_argument?

Answers:

a. "my_parser" is our version of "argparse" engine.
b. we have added "rule" (our command line parameter(s)) to the "rule".
c. "args = my_parser.parse_args()" is where the actual Python script (this script)'s parameters
 being "fed" into our command line parameters parsing engine. After which the rules (added in b.)
 will be applied then returns the result to "args"

5) tail=args.tail_filename - is this a definition assignment for tail_filename above?

Correct!

6) I see where the fin (filename) has the stationary name + tail -

            does this +tail relate back to the tail definition for args.tail_filename?

"Tail" is the string we had inputted at the command line. Concatenated with
7) How can I test this code?

"""

import argparse
import csv

# import os
# import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='File processing ... ')

# Add the arguments
my_parser.add_argument('--jack_filename',
                       action='store',
                       type=str,
                       dest="tail_filename",
                       required=True,
                       help='the tail part of the file name')

# Execute the parse_args() method
args = my_parser.parse_args()

# Where "tail" might look like this: '20160101_20200713_20200713'
tail = args.tail_filename

fin = 'mlb_players_' + tail

fin_name_without_extention = fin.strip('.csv')

with open(fin, 'r') as fi:
    csv_reader = csv.reader(fi, delimiter=',')
    line_count = 0
    try:
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(
                    f'\t{row[0]} was with {row[1]}, his was {row[2]}. The weight/height/age: {row[3]}/{row[4]}/{row[5]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
    except ValueError as err:
        print(f"ERR: {err}")



