import csv
from pathlib import Path
from noun import Noun

PATH = Path(__file__).parent.parent.joinpath('noun_list.csv')
CSV_HEADER = ['Noun', 'Article', 'Plural', 'Translation', 'Date Last Correct', 'Correct Streak']

def list_to_noun(noun_list: list) -> Noun:
    noun = Noun(noun_list[0])
    noun.article = noun_list[1]
    noun.plural = noun_list[2]
    noun.translation = noun_list[3]
    noun.date_last_correct = noun_list[4]
    noun.correct_streak = noun_list[5]
    return noun

def print_all_nouns():
    with open(PATH, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        line_number = 0
        for line in csv_reader:
            if line_number != 0:
                print(f'{line[1]} {line[0]}')
                line_number += 1
            else:
                line_number += 1

# Could implement a better searching algo
def find_noun_in_csv(word: str) -> list:
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
                noun_object = list_to_noun(row)
                matching_nouns.append(noun_object)
            else:
                line_count +=1
    return matching_nouns

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

#TODO: Remove header on input (it is added back in the write function)
def read_csvfile_to_list() -> list:
    data = []
    with open(PATH, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        line_number = 0
        for row in csv_reader:
            if line_number != 0:
                data.append(row)
            line_number += 1
    return data

def write_list_to_csvfile(sorted_list: list):
    with open(PATH, 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerows(sorted_list)

def sort_csv_list(data_list: list) -> list:
    # Removes header, sorts, then inserts header
    if data_list[0] == CSV_HEADER: 
        data_list.pop(0)
    data_list.sort()
    data_list.insert(0, CSV_HEADER)
    return data_list

def remove_duplicates(data: list) -> list:
    popped = []
    while len(data) > 1:
        item = data.pop(0)
        if item not in data:
            popped.append(item)
    return popped + data


def add_noun_to_csv(noun_object: Noun):
    data = read_csvfile_to_list()
    noun_list = noun_object.to_list_format()
    print(noun_list)
    print(data[2])
    print(f'Checking if it\'s in the list: {noun_list in data}')
    if noun_list in data:
        print('The noun is already in the list. Returning.')
        return
    data.append(noun_list)
    data = sort_csv_list(data)
    write_list_to_csvfile(data)

#Does not handle duplicates
def remove_noun_from_csv(noun_object: Noun):
    data = read_csvfile_to_list()
    noun_list = noun_object.to_list_format()
    for item in data:
        if item == noun_list:
            data.remove(item)
    write_list_to_csvfile(data)

if __name__ == '__main__':
    data = read_csvfile_to_list()
    for n in data:
        print(n)