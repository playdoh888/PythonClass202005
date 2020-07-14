import argparse

my_parser = argparse.ArgumentParser(prog='ex18', description='List the content of a folder')

my_parser.add_argument('--input', action='store', type=str, dest="infile", required=True, help='The file to be copied')
my_parser.add_argument('--output', action='store', type=str, dest="outfile", required=True, help='The new file')
my_parser.add_argument('--count', action='store', type=int, default='9', help='Integer used to replace letter "e"')

args = my_parser.parse_args()

with open(args.infile) as in_file, open(args.outfile, 'w') as out_file:
    for line in in_file:
        if args.count:
            parsed_line = line.replace('e', str(args.count))
        else:
            parsed_line = line.replace('e', 'E')
        out_file.write(parsed_line)


print(f"Input file name: {args.infile}")
print(f"Input file name: {args.outfile}")
