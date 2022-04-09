import os

print(
    'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG' + "  Hello, welcome to my convenient all in one python script. I made \n" 
    'GGGGGGGGGGG GG            GGGGGGGGGGGGGG' + "  this to shut someone up in my dms because I dislike scripting \n"
    'GGGGGGGGG                      GGGGGGGGG' + "  languages. \n"
    'GGGGGGGG                         GGGGGGG \n'
    'GGGG G           GGGGGGGG         GGGGGG \n'
    'GGGG          GGGGG     G G         GGGG \n'
    'GGG          GGGG                    GGG \n'
    'GGG         GGG                      G G \n'
    'GG         GGG                        GG \n'
    'GG         GGG            G           GG \n'
    'GG          GGG           GG          GG \n'
    'GG           GG           GG          GG \n'
    'GGG           GGGG GGGGGGGG          GGG \n'
    'GG G             GGG GGGGGG         G GG \n'
    'GGGGG                              G GGG \n'
    'GGGGGG                            GGGGGG \n'
    'GGGGGGGG                        GGGGGGGG \n'
    'GGGGGGGGGGG                   GGGGGGGGGG \n'
    'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG \n'
    'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG \n'
    
    "1. Automatic Installations \n"                                        
    "2. Network Tools \n"
    "3. Penetration Testing \n"
)

match input("Please choose one: "):
    case "1":
        with open(os.path.join(os.path.dirname(__file__), "installations/installations.py"), 'r') as file:
            exec(file.read())
    case "2":
        with open(os.path.join(os.path.dirname(__file__), "networking/networking.py"), 'r') as file:
            exec(file.read())
    case "3":
        with open(os.path.join(os.path.dirname(__file__), "pentest/pentest.py"), 'r') as file:
            exec(file.read())