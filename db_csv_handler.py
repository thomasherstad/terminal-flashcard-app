import csv
from src.noun import Noun

PATH = 'noun_list.csv'

def print_all_nouns():
    with open(PATH) as file:
        csv_reader = csv.reader(file, delimiter=';')
        line_number = 0
        for line in csv_reader:
            if line_number != 0:
                print(f'{line[1]} {line[0]}')
                line_number += 1
            else:
                line_number += 1

#Could implement a better searching algo if it's for sure sorted
#Returns an empty list when no matches. Should I change to none?
def find_noun_in_csv(word):
    word = word.lower().capitalize()
    matching_nouns = []
    with open(PATH) as file:
        csv_reader = csv.reader(file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif row[0] == word:
                #Potential for problem when changing csv table size
                noun = Noun(row[0])
                noun.article = row[1]
                noun.plural = row[2]
                noun.translation = row[3]
                noun.date_last_correct = row[4]
                noun.correct_streak = row[5]
                matching_nouns.append(noun)
            else:
                line_count +=1
        if matching_nouns == []:
            return None
    return matching_nouns

#matching_nouns is a list of Noun objects
def display_found_nouns(matching_nouns):
    amount = len(matching_nouns)
    if amount == None:
        print('There were no matches in the list')
    elif amount > 0:
        print(f'{amount} results were found matching "{matching_nouns[0].noun}": ')
        for noun in matching_nouns:
            print(noun)        
    else:
        raise Exception('Search function must have returned something other than a list')


def create_noun_user():
    word = input('Which noun do you want to add?\n').capitalize()
    noun = Noun(word)
    noun.get_article_from_user()
    noun.get_plural_from_user()
    noun.get_translation_from_user()
    return noun


def append_noun_to_list(noun_tuple):
    with open(PATH) as file:
        csv_writer = csv.writer(file, delimiter=';')


def check_if_noun_should_be_added(noun):
    if find_noun_in_csv(noun) is None:
        pass



if __name__ == '__main__':
    results = find_noun_in_csv('see')
    display_found_nouns(results)