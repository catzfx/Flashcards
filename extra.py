import os

title = 'Flashcards 0.0.1\n||Terminal Edition||\n'

def wipe(quit=False):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    if quit == False:
        print(title)