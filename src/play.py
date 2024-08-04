from noun import Noun
from noun_list import NounList

#How to best choose the nouns to play with?
def extract_subset_sorted_deck(deck: NounList, amount: int) -> NounList:
    
    subset_list = deck.noun_list[:15]
    subset_deck = NounList(subset_list)
    return subset_deck

def play_noun():
    pass

#Algorithm needs to be figured out
def play_normal(deck: NounList):
    #stop_criteria
    #current algorithm: Just loop through the list three times
    for i in range(0, 3):
        for item in deck:
            pass