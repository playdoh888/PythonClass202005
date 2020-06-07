import os

def person():
    name = "Sarah"
    age = 26
    print(f"person details {name}, {age}")

script_name = os.path.basename(__file__)
print(f"top-level in {script_name} module")

if __name__ == "__main__":
    print(f"{script_name} module is run directly")
else:
    print(f"{script_name} module is imported into another module")

