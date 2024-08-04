import os
import time

from noun import Noun
from noun_list import NounList
from db_csv_handler import read_csvfile_to_list,  write_list_to_csvfile

#TODO: Add windows/linux/mac support depending on os
def clear_terminal():
    os.system('clear')

def load_noun_list() -> NounList:
    deck = NounList()
    deck.append_from_list(read_csvfile_to_list())
    return deck

def save_noun_list(nouns: NounList):
    print('Saving changes', end='')
    nouns.export_to_csv()
    print(' Changes saved')

#TODO: Add fail safe for inputs outside of choices
def make_menu(header: str, menu_options: list, back=False, back_label='Back') -> int:
    #Returns list index
    number = 1
    print(header)
    for item in menu_options:
        print(f'{number}. {item}')
        number += 1
    if back == True:
        print(f'0. {back_label}')
    menu_choice = int(input())
    clear_terminal()
    return menu_choice - 1

def main_menu() -> int:
    menu_options = ['Play', 'View List', 'Add Noun', 'Search List', 'Edit Noun', 'Save & Close']
    choice = make_menu('Welcome to Flashcards!', menu_options)
    return choice

def play_menu():
    options = ['Standard (15 Nouns)', 'Endless', 'Custom']
    choice = make_menu('Game Menu', options)
    return choice

def play(nouns: NounList):
    choice = play_menu()
    if choice == 1:
        print('You have chosen Standard')
    elif choice == 2:
        print('You have chosen Endless')
    elif choice == 3:
        print('You have chosen Custom')

def view_list(nouns: NounList) -> None:
    print(nouns)
    ans = make_menu('', [], back=True)
    if ans == -1:
        return
    
def add_noun_to_list(nouns: NounList) -> NounList:
    noun = Noun(input('Which noun do you want to add?\n').lower().capitalize())
    noun.get_article_from_user()
    noun.get_plural_from_user()
    noun.get_translation_from_user()
    if not nouns.in_list(noun):
        nouns.add_noun(noun)
        print(f'{noun} has been added to the list.')
    else:
        print(f'{noun} is already in the list. Nothing added.')
    return nouns

def search_list(nouns: NounList) -> None:
    word = input('Which noun do you want to search for?\n').lower().capitalize()
    results = nouns.search_word(word)
    if results.noun_list == []:
        print(f'"{word}" was not found in the list.')
    elif len(results.noun_list) == 1:
        print(f'1 match was found for "{word}":')
        print(results)
    else:
        print(f'{len(results.noun_list)} matches were found for "{word}":')
        print(results)
        

def edit_noun(old_noun: Noun, nouns: NounList) -> NounList:
    new_noun = old_noun
    nouns.remove_noun(old_noun)

    while True:
        print(new_noun)
        options = ['Noun', 'Article', 'Plural', 'Translation']
        ans =  make_menu('What do you want to edit?', options, back=True, back_label='Done')
        if ans == -1:
            break
        elif options[ans] == 'Noun':
            print('Edit Noun')
        elif options[ans] == 'Article':
            print(new_noun)
            new_noun.get_article_from_user()
        elif options[ans] == 'Plural':
            print(new_noun)
            new_noun.get_plural_from_user()
        elif options[ans] == 'Translation':
            print(new_noun)
            new_noun.get_translation_from_user()
    nouns.add_noun(new_noun)

    save_noun_list()
    return nouns

def choose_noun_to_edit(nouns: NounList) -> Noun:
    while True:
        word = input('Which noun do you want to choose?\n').lower().capitalize()
        results = nouns.search_word(word).noun_list
        if results == []:
            print(f'{word} is not in the list, try again')
            continue
        elif len(results) == 1:
            noun = results[0]
        else:
            print('There is more than one result')
            noun_choice = make_menu('Which noun do you want to choose?\n', results)
            noun = results[noun_choice]
        return noun



def main():
    deck = load_noun_list()
    
    while True:
        choice = main_menu()
        if choice == 0:
            play(deck)
        elif choice == 1:
            view_list(deck)
        elif choice == 2: 
            deck = add_noun_to_list(deck)
        elif choice == 3:
            search_list(deck)
        elif choice == 4:
            while True:
                noun = choose_noun_to_edit(deck)
                deck = edit_noun(noun, deck)
                options = ['Yes', 'No']
                ans = make_menu('Do you want to edit another noun?', options)
                if options[ans] == 'No':
                    break
        elif choice == 5:
            save_noun_list(deck)
            break
    clear_terminal()


        
    

if __name__ == '__main__':
    main()
