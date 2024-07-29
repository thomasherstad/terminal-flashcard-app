from noun import Noun
from noun_list import NounList
from db_csv_handler import read_csvfile_to_list,  write_list_to_csvfile

def load_noun_list() -> NounList:
    deck = NounList()
    deck.append_from_list(read_csvfile_to_list())
    return deck

#TODO: Add fail safe for inputs outside of choices
def make_menu(header: str, menu_items: list) -> int:
    number = 1
    print(header)
    for item in menu_items:
        print(f'{number}. {item}')
        number += 1
    menu_choice = int(input())
    return menu_choice - 1 #Returns list index

def main_menu() -> int:
    menu_options = ['Play', 'View List', 'Add Noun', 'Search List', 'Edit Noun', 'Close']
    choice = make_menu('Welcome to Flashcards!', menu_options)
    return choice

def play_menu():
    options = ['15 Nouns', 'Endless', 'Custom']
    choice = make_menu('Game Menu', options)
    return choice

def play(nouns: NounList):
    choice = play_menu()
    if choice == 1:
        print('You have chosen 15 Nouns')
    elif choice == 2:
        print('You have chosen Endless')
    elif choice == 3:
        print('You have chosen Custom')

def view_list(nouns: NounList):
    print(nouns)

def add_noun_to_list(nouns: NounList):
    pass

def search_list(nouns: NounList):
    pass

def edit_noun(nouns: NounList):
    pass

def close(nouns: NounList):
    nouns.export_to_csv()

def main():
    deck = load_noun_list()
    choice = main_menu()
    
    if choice == 1:
        play(deck)
    elif choice == 2:
        view_list(deck)
    elif choice == 3: 
        add_noun_to_list(deck)
    elif choice == 4:
        search_list(deck)
    elif choice == 5:
        edit_noun(deck)
    elif choice == 6:
        close(deck)


        
    

if __name__ == '__main__':
    main()
