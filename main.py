import subprocess
from wipe import wipe

##### FLASHCARDS ATESTAT INFO 2024 ####
 #### made by CRACIUN IUSTIN-ANDI ####
  ###        functia main         ###

wipe()
print('Welcome to Flashcards by Craciun Iustin Andi.\n')
print('1. Enter Learning Mode')
print('2. Enter Card Manager Mode')
print('3. Change Ease Settings')
print('4. Help (explanation of how the application works)')
print('5. Quit')
option = int(input('> '))
if option == 5:
    wipe(quit=True)
elif option == 4:
    print("    Flashcards is a learning app that works on the principle of spaced repetition: if you review a piece of knowledge repeatedly, it will enter your long term memory. Each time you review, the time that knowledge remains in your mind increases, which means that eventually you will only see a card every few months, because it (presumably) is already engrained in your brain.\n    Cards: Cards are pairs of questions and answers. When in Learning Mode, you will first only see the question, and you will try to remember what the answer was. After revealing the answer, if you turned out to be wrong, you will let the program know, and it'll show you that card sooner in the future. If you knew the answer, it'll show you that card less in the future.\n    Ease: Ease refers to the algorithm governing the frequency at which you're shown specific cards. In this program, the first 5 values are specified, and all values above that increase exponentially with powers of two.\n    The Card Manager: The Card Manager is the tool with which you can manage your local card database by adding or removing cards and such.")
    input("\nPress -enter- to return to top")
    subprocess.run(['python','./main.py'])
elif option == 1:
    subprocess.run(['python','./learner.py'])
elif option == 2:
    subprocess.run(['python','./card_manager.py'])
elif option == 3:
    subprocess.run(['python','./edit_settings.py'])