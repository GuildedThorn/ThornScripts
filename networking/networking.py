import os

os.system("clear")
print(
    "1. Nmap Scan \n"
    "2. Pinger \n"
    "3. Endpoint Scan \n"
    "99. Back \n"
)

match input("Please choose one: "):
    case "1":
        address = input("\nPlease input an ip address: ")
        os.system(f"nmap -sC -sV {address}")
    case "2":
        address = input("\nPlease input an ip address: ")
        os.system(f"ping {address}")
    case "3":
        address = input("\nPlease input an ip address: ")
        os.system(f"dirb {address}")
    case "99":
        with open(os.path.join(os.path.dirname(__file__), "main.py"), 'r') as file:
            exec(file.read())
