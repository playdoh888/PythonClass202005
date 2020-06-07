types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
binary = "integer"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")
hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
print("Isn't that joke so funny?! {}".format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
d = " Jack!"
long_string = w + e + d
print(long_string)

new_long_string = long_string.replace('Jack', 'Wang')
print(new_long_string)
