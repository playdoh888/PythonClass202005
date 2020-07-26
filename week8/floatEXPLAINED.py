"""
Exact equality between floating-point numbers is a dangerous concept. After a lengthy computation,
round-off errors in floating point numbers may have infinitesimally small differences.
The answers are close enough to equal for all practical purposes,
but every single one of the 64 bits may not be identical.

The following technique is the appropriate way to do floating point comparisons.

abs(a-b)<0.0001
Rather than ask if the two floating point values are the same,
we ask if they're close enough to be considered the same. For example, run the following tiny program.

"""

# Are two floating point values really completely equal?
a,b = 1/3.0, .1/.3
print(a,b,a==b)
print(abs(a-b)<0.00001)

"""
The two values appear the same when printed. Yet, on most platforms, 
the == test returns False. They are not precisely the same. 
This is a consequence of representing real numbers with only a finite amount of binary precision. 
Certain repeating decimals get truncated, and these truncation errors accumulate in our calculations.

There are ways to avoid this problem; one part of this avoidance is to do the algebra necessary to 
postpone doing division operations. Division introduces the largest number erroneous bits onto 
the trailing edge of our numbers. The other part of avoiding the problem is never to compare floating point numbers 
for exact equality.

"""

