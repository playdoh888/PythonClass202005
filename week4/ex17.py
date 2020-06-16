import random
import time

start = time.time()
l = [random.randint(1, 999) for _ in range(10 * 3)]

end = time.time()
print(end - start)


start = time.time_ns()
l = [random.randint(1, 999) for _ in range(10 * 3)]

end = time.time_ns()
print(end - start)
