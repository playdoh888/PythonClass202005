"""
The ABC organics company needs a simple program that their call center will use to enter survey data for a new coffee variety.
The program must accept input and return the average rating based on a five-star scale.
The output must be rounded to two decimal places.
You need to complete the code to meet the requirements.
How should you complete the code? To answer, select the appropriate code segments in the answer area.
NOTE: Each correct selection is worth one point.
"""

sum = count = done = 0
average = 0.0

while (done != -1):
    rating =
#  print("Enter next rating (1-5), -1 for done")
#* float(input("Enter next rating (1-5), -1 for done")) *
#  input "Enter next rating (1-5), -1 for done")
#  input("Enter next rating (1-5), -1 for done: ")

    if rating == -1:
        break

    sum += rating
    count += 1

average = float(sum/count)

#  output("The average star rating for the new coffee is:" +
#  console.input('The average star rating for the new coffee is:" +
#  printline("The average star rating for the new coffee is:" +
#* print("The average star rating for the new coffee is:" +


#* format(average, '.2f'))
# format(average, '2d'))
# {average, '2f})
# format.average.{2d}

print("The average star rating for the new coffee is:" + format(average, '.2d'))
"""
Return value from format()
The format() function returns a formatted representation of a given value specified by the format specifier.

Example 1: Number formatting with format()
# d, f and b are type

# integer
print(format(123, "d"))

# float arguments
print(format(123.4567898, "f"))

# binary format
print(format(12, "b"))
"""
