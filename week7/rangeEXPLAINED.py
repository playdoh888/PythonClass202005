# "for" loop explained:
# All the for construct does is loop over an iterable.
# If that iterable is empty, then the body of the for is never executed.
#
# "range" explained:
# All range does is return an interable containing all the values from start to stop
# (inclusive of start, exclusive of stop).
# If start is higher than stop,
# then the iterable is empty because there are no valid values between start and stop:

L = []
for i in range(-1,-2):
    L.append(i)
    print(f"i: {i}")

print((f"L: {L}"))



