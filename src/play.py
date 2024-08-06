from noun import Noun
from noun_list import NounList
from db_csv_handler import read_csvfile_to_list
from menu import make_menu


def play_noun(noun: Noun) -> str:
    feedback_options = ['again', 'hard', 'good', 'easy']
    articles = ['Der', 'Die', 'Das']
    print(noun.card_front)
    article_choice = make_menu('What is the article?', articles, back=True, back_label='Cancel')
    if article_choice == -1:
        return None
    elif articles[article_choice] == noun.article:
        print('Correct!')
    else:
        print('Wrong!')
    print(noun.card_back)
    feedback_choice = make_menu('How difficult was it?', feedback_options, back=True, back_label='Cancel')
    if feedback_choice == -1:
        return None
    return feedback_options[feedback_choice]
    

def play_top_noun(deck: NounList):
    noun = deck.noun_list[0]
    if noun.is_due:
        feedback = play_noun(noun)
        if feedback == None:
            print('Feedback = None')
            return deck
        noun.feedback(feedback)
    else:
        print('No nouns due')
    return deck

if __name__ == '__main__':
    print('Play.py: is main')
    deck = NounList()
    deck.append_from_list(read_csvfile_to_list())
    play_top_noun(deck)
