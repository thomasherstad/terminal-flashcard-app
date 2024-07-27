import csv

PATH = 'noun_list.csv'

def read_db():
     with open(PATH) as file:
        return csv.reader(file, delimiter=';')

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
#Using a tuple to store the nouns at the moment
def find_noun_in_csv(noun):
    noun = noun.capitalize()
    matching_nouns = []
    with open(PATH) as file:
        csv_reader = csv.reader(file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif row[0] == noun:
                #at some point refactor to use a loop
                noun_tuple = (row[0], row[1], row[2], row[3], row[4], row[5])
                matching_nouns.append(noun_tuple)
            else:
                line_count +=1
    return matching_nouns

#matching nouns is a list of tuples
def display_found_nouns(matching_nouns):
    amount = len(matching_nouns)
    if amount == 0:
        print('There were no matches in the list')
    elif amount > 0:
        print(f'{amount} results were found: ')
        for noun_tuple in matching_nouns:
            print(f'{noun_tuple[1]} {noun_tuple[0]}, which means "{noun_tuple[3]}"')        
    else:
        raise Exception('Search function must have returned something other than a list')

if __name__ == '__main__':
    noun = input('Which noun do you want to search for?\n')
    results = find_noun_in_csv(noun)
    display_found_nouns(results)