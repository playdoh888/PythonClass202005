"""
    csv.field_size_limit – return maximum field size
    csv.get_dialect – get the dialect which is associated with the name
    csv.list_dialects – show all registered dialects
    csv.reader – read data from a csv file
    csv.register_dialect - associate dialect with name
    csv.writer – write data to a csv file
    csv.unregister_dialect - delete the dialect associated with the name the dialect registry
    csv.QUOTE_ALL - Quote everything, regardless of type.
    csv.QUOTE_MINIMAL - Quote fields with special characters
    csv.QUOTE_NONNUMERIC - Quote all fields that aren't numbers value
    csv.QUOTE_NONE – Don't quote anything in output

"""
import csv

with open('oscar_age_female.csv', mode='r') as read_csv_file:
    csv_reader = csv.DictReader(read_csv_file, quotechar='"',  doublequote=False, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Name"]} won the {row["Year"]} Academy Award for Best Actress')
        line_count += 1
    print(f'Processed {line_count} lines.')
