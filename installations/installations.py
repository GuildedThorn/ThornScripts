import os

os.system("clear")
print(
    "1. MariaDB \n"
    "99. Back \n"
)

match input("Please choose one: "):
    case "1":
        os.system("sh ./MariaDB.sh")
    case "99":
        with open(os.path.join(os.path.dirname(__file__), "main.py"), 'r') as file:
            exec(file.read())
