import os

os.system("clear")
print(
    "------------------------------------------------------------------------------\n"
    "  Hello, welcome to my convenient all in one kali linux python script. I made \n"
    "  this to shut someone up in my dms because I dislike scripting languages \n\n"
    "  Website: https://guildedthorn.com/ \n"
    "  Github: https://github.com/GuildedThorn \n"
    "  Email: GuildedThorn@gmail.com \n"
    "------------------------------------------------------------------------------\n"
    "\n"
    "1. Automatic Installations \n"
    "2. Network Tools \n"
    "3. Wifi Attacks"
)

match input("Please choose one: "):
    case "1":
        with open(os.path.join(os.path.dirname(__file__), "installations/installations.py"), 'r') as file:
            exec(file.read())
    case "2":
        with open(os.path.join(os.path.dirname(__file__), "networking/networking.py"), 'r') as file:
            exec(file.read())
    case "3":
        with open(os.path.join(os.path.dirname(__file__), "wifi-attacks/wifi-attacks.py"), 'r') as file:
            exec(file.read())
