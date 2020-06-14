x = 1
try:
    print(x)
    y = x + 1
    z = 0
    print( y / z)
    for i in range(1, 10):
      print(i)
except Exception as err:
    print(f"An exception occurred. Detail information: {err}")
