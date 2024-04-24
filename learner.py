from tinydb import TinyDB, Query
import datetime
from wipe import wipe

db = TinyDB('./db.json')
settings = TinyDB('./settings.json')
ease_list = settings.get(doc_id=1).get('ease')
due_count = 0

def due_search():
    due_list = []
    for card in db:
        delta = datetime.datetime.now() - datetime.datetime.strptime(card.get('due'), "%Y-%m-%d %H:%M:%S.%f")
        if delta.days >= 0:
            due_list.append((card, card.doc_id))
    return due_list
        
    
wipe()
due_list = due_search()
print(f'{len(due_list)} cards due')
input('Press -enter- to enter learning mode\n(you can press ctrl-c at any time to quit)\n')

while len(due_list) > 0:
    for due_card, due_id in due_list:
        wipe()
        print(f'ID: {due_id}', end= "  ")
        print(f'Category: {due_card.get("category")}')
        print(f'Q: {due_card.get("q")}')
        input('\nPress -enter- to show answer\n')
        wipe()
        print(f'ID: {due_id}', end= "  ")
        print(f'Category: {due_card.get("category")}')
        print(f'Q: {due_card.get("q")}')
        print(f'A: {due_card.get("a")}')
        print('\nf. I knew it  ----   j. Again')
        option = input("> ")
        if option == 'f':
            card_ease = due_card.get('count')
            time_change = datetime.timedelta(minutes = 2)
            if card_ease < 5:
                time_change = datetime.timedelta(minutes=ease_list[card_ease])

            else:
                time_change = datetime.timedelta(minutes=1440 * pow(2, card_ease - 4))

            db.update({'due': str(datetime.datetime.now() + time_change),
                       'count': card_ease + 1}, doc_ids=[due_id])
        elif option == 'j':
            card_ease = due_card.get('count')
            if card_ease > 5:
                card_ease = 3
            else:
                card_ease = 0
            time_change = datetime.timedelta(minutes = ease_list[card_ease])
            db.update({'count': card_ease,
                       'due': str(datetime.datetime.now() + time_change)},doc_ids=[due_id])
    due_list = due_search()