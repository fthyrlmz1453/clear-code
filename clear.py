# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
clear()