import dis, math, sys

def square_root(x): return math.sqrt(x)
print(f"function square_root() is located at: {square_root}")
dis.dis(square_root)

square_root = lambda x: math.sqrt(x)
print(f"the lambda function of square_root() is located at: {square_root}")
dis.dis(square_root)

sum = lambda x, y: x + y  # def sum(x,y): return x + y

