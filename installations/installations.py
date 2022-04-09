import os

print(
    "1. MariaDB"
)

match input("Please choose one: "):
    case "1":
        os.system("sh ./MariaDB.sh")