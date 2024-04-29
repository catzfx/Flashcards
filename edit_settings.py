from tinydb import TinyDB, Query
from extra import wipe

settings_db = TinyDB('./settings.json')
Setting = Query()


while True:
    wipe()
    ease_list = settings_db.get(doc_id=1).get('ease')

    print('Current settings: ')
    for e in ease_list:
        print(f'After {ease_list.index(e) + 1} time{"s" if ease_list.index(e) != 0 else ""}: {e} minute{"s" if e != 1 else ""}')

    print("After more times, the value will just double.")
    
    option = int(input("\nwhich value do you wish to modify (ctrl-c to cancel)?\n> "))
    value = int(input(f'The {option}{"st" if option == 1 else "nd" if option == 2 else "rd" if option == 3 else "th"} value will change from {ease_list[option - 1]} to:\n> '))

    ease_list[option - 1] = value

    settings_db.update({'ease': ease_list}, doc_ids=[1])
    input('Press -enter- to go back to top (or ctrl-c to quit)\n')


