from noun import Noun
from db_csv_handler import read_csvfile_to_list, write_list_to_csvfile

class NounList:
    def __init__(self):
        self.noun_list = []
        

    def populate_from_list(self, data: list):
        for item in data:
            noun = Noun(item[0], item[1], item[2], item[3])
            self.noun_list.append(noun)
    
    def __repr__(self):
        result = ''
        for item in self.noun_list:
            result += str(item)
            if item != self.noun_list[-1]:
                result += '\n'
        return result

if __name__ == '__main__':
    nouns = NounList()
    nouns.populate_from_list(read_csvfile_to_list())
    print(nouns)