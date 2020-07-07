#import necessary modules
import csv

def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`,
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

with open('oscar_age_female.csv', mode='r') as read_csv_file, open('new_oscar_age_female.csv', mode='w+') as write_csv_file:
    csv_reader = csv.DictReader(read_csv_file, quotechar='"',  doublequote=False, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    line_count = 0
    for row in csv_reader:
        writer = csv.DictWriter(write_csv_file, quotechar='"',  doublequote=False, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True, fieldnames=row)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            writer.writeheader()
        # item = { k: eval(v) if is_number(v) else v for k, v in row.items()  }
        writer.writerow(row)
        line_count += 1
        print(f'\t{row["Name"]} won the {row["Year"]} Academy Award for Best Actress')
    print(f'Processed {line_count} lines.')

with open('new_oscar_age_female.csv', mode='a+') as write_csv_file:
    writer = csv.DictWriter(write_csv_file, quotechar='"', doublequote=False, delimiter=',', quoting=csv.QUOTE_ALL,
                            skipinitialspace=True, fieldnames=row)
    line_count += 1
    row = { "Index" : str(line_count),
        "Year" : "2017",
        "Age" : "31",
        "Name" : "Emma Stone",
        "Movie" : "La La Land",
    }
    writer.writerow(row)
    line_count += 1
    row = {"Index": str(line_count),
           "Year": "2018",
           "Age": "63",
           "Name": "Frances McDormand",
           "Movie": "Three Billboards Outside Ebbing, Missouri",
           }
    writer.writerow(row)
    line_count += 1
    row = {"Index": str(line_count),
           "Year": "2019",
           "Age": "46",
           "Name": "Olivia Colman",
           "Movie": "The Favourite",
           }
    writer.writerow(row)
    line_count += 1
    row = {"Index": str(line_count),
           "Year": "2020",
           "Age": "51",
           "Name": "Renée Zellweger",
           "Movie": "Judy",
           }
    writer.writerow(row)
print(f'Processed {line_count} lines.')


# 2017, 31,"Emma Stone","La La Land"
# 2018, 63,"Frances McDormand","Three Billboards Outside Ebbing, Missouri"
# 2019, 46,"Olivia Colman","The Favourite"
# 2020, 51,"Renée Zellweger","Judy"