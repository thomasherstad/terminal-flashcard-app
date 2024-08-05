import csv
from pathlib import Path
from noun import Noun

PATH = Path(__file__).parent.parent.joinpath('noun_list.csv')
CSV_HEADER = ['Noun', 'Article', 'Plural', 'Translation', 'Status', 'Step', 'Ease', 'Next Review']

#Obsolete?
def list_to_noun(noun_list: list) -> Noun:
    noun = Noun(noun_list[0])
    noun.article = noun_list[1]
    noun.plural = noun_list[2]
    noun.translation = noun_list[3]
    noun.next_review = noun_list[4]
    noun.correct_streak = noun_list[5]
    return noun

# matching_nouns is a list of Noun objects
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


def create_noun_user() -> Noun:
    word = input('Which noun do you want to add?\n').capitalize()
    noun = Noun(word)
    noun.get_article_from_user()
    noun.get_plural_from_user()
    noun.get_translation_from_user()
    return noun

def read_csvfile_to_list() -> list[list]:
    data = []
    with open(PATH, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        line_number = 0
        for row in csv_reader:
            if line_number != 0:
                data.append(row)
            line_number += 1
    return data

def write_list_to_csvfile(data: list):
    data.insert(0, CSV_HEADER)
    with open(PATH, 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerows(data)

def remove_duplicates(data: list) -> list:
    popped = []
    while len(data) > 1:
        item = data.pop(0)
        if item not in data:
            popped.append(item)
    return popped + data

if __name__ == '__main__':
    data = read_csvfile_to_list()
    for n in data:
        print(n)