import os

print(
    "1. Nmap Scan \n"
    "2. Pinger \n"
    "3. Endpoint Scan \n"
)

# TODO Write shell script for each of these
match input("Please choose one: "):
    case "1":
        address = input("\n Please input an ip address: ")
        os.system(f"nmap -sC -sV {address}")
    case "2":
        address = input("\n Please input an ip address: ")
        os.system(f"ping {address}")
    case "3":
        address = input("\n Please input an ip address: ")
        os.system(f"dirb {address}")