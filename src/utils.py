import os
import colorama

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

