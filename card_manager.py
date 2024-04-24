from tinydb import TinyDB, Query
from datetime import datetime
from wipe import wipe
db = TinyDB('./db.json')
cardq = Query()
print('\n\n::Card Manager::')

while True:
    wipe()
    print('Card Manager\n\n1. list all\n2. add card\n3. remove card\n4. Quit')
    print('> ', end='')
    option = int(input())
    if option == 4:
        wipe(quit=True)
        break
    elif option == 3:
        card_id = int(input('card id to delete: '))
        db.remove(doc_ids=[card_id])
    elif option == 2:
        card_category = input('card category: ')
        card_qtion = input('card question: ')
        card_answ = input('card asnwer: ')
        db.insert({'category': card_category,
                   'q': card_qtion,
                   'a': card_answ,
                   'count': 0,
                   'due': str(datetime.now())
                   })
    elif option == 1:
        for card in db:
            print(card.doc_id, end='. ')
            cat = card.get('category')
            que = card.get('q')
            ans = card.get('a')
            ease = card.get('count')
            due_date = card.get('due')
            print(f'Category: {cat} || Question: {que} || Answer: {ans} || Ease value: {ease} || Due date: {due_date}\n')
    input('\nPress -enter- to go back to top\n')