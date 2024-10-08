from noun import Noun
from db_csv_handler import read_csvfile_to_list, write_list_to_csvfile

class NounList:
    def __init__(self, nouns = []):
        self.noun_list = nouns

    def append_from_list(self, data: list):
        for item in data:
            noun = Noun(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])
            self.noun_list.append(noun)

    def __repr__(self):
        result = ''
        for item in self.noun_list:
            result += str(item)
            if item != self.noun_list[-1]:
                result += '\n'
        return result
    
    def __eq__(self, other):
        if self.noun_list == other.noun_list:
            return True 
        return False


    def search_word(self, word: str): # Returns a NounList
        word = word.lower().capitalize()
        matches = NounList([])
        for noun in self.noun_list:
            if noun.noun == word:
                matches.add_noun(noun)
        return matches

    def in_list(self, noun: Noun) -> bool:
        if noun in self.noun_list:
            return True
        return False

    def sort(self):
        self.noun_list.sort()

    def get_next_review(noun):
        return noun.next_review

    def sort_time(self):
        self.noun_list.sort(key=lambda x: x.next_review)

    def update_is_due_nouns(self):
        for noun in self.noun_list:
            noun.update_is_due()

    def add_noun(self, noun: Noun):
        if self.in_list(noun) != True:
            self.noun_list.append(noun)
            self.sort()

    # Does not handle duplicates
    # Only works if the translation is exactly the same
    def remove_noun(self, noun: Noun):
        if self.in_list(noun):
            self.noun_list.remove(noun)

    def export_to_csv(self):
        data = []
        self.sort()
        for noun in self.noun_list:
            data.append(noun.to_list_format())
        write_list_to_csvfile(data)

if __name__ == '__main__':
    nouns = NounList()
    nouns.append_from_list(read_csvfile_to_list())
    nouns.sort()
    print(nouns)
    print('---------------------------------')
    print(nouns)
    print('---------------------------------')
    nouns.sort_time()
    print(nouns)
    nouns.export_to_csv()