import os
import tagline

def wipe(quit=False):
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    if quit == False:
        print(tagline.title)