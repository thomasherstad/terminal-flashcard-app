from datetime import datetime, timedelta

class Noun():
    def __init__(self, noun, article=None, plural=None, translation=None, status=None, step=None, ease=None, next_review=datetime.now()):

        self.article = article
        self.noun = noun
        self.plural = plural
        self.translation = translation
        self.status = status
        self.step = step
        self.ease = ease 
        self.next_review = next_review
        self.card_front = f'... {self.noun} - ({self.translation})'
        self.card_back = str(self)
    
    
    def __str__(self):
        if self.translation and self.plural and self.article:
            return f'{self.article} {self.noun}, Die {self.plural} ({self.translation})'
        elif self.plural and self.article:
            return f'{self.article} {self.noun}, Die {self.plural}'
        elif self.article:
            return f'{self.article} {self.noun}'
        else:
            return f'{self.noun} - Missing Information'

    def __repr__(self):
        return str(self)

    # Is this needed?
    def __eq__(self, other):
        if self.article == other.article and self.noun == other.noun and self.plural == other.plural and self.translation == other.translation:
            return True
        return False
    
    def __lt__(self, other):
        return self.noun < other.noun

    def get_article_from_user(self):
        articles = ['Der', 'Die', 'Das']
        while True:
            print(f'Which article does {self.noun} have?')
            answer = int(input('1.Der\t 2.Die\t 3.Das\n'))
            if answer in [1, 2, 3]:
                break
        self.article = articles[answer - 1]

    def get_plural_from_user(self):
        self.plural = input(f'What is the plural of {self.noun}?\n').lower().capitalize()

    def get_translation_from_user(self):
        self.translation = input(f'What does {self.noun} mean?\n').lower().capitalize()
    
    # TODO: Is this really needed?
    def to_csv_format(self) -> str:
        return f'{self.noun};{self.article};{self.plural};{self.translation};{self.status};{self.step};{self.ease};{self.next_review}'
                
    
    #TODO: There is probably a way to override something so I can use list(noun)
    def to_list_format(self) -> list:
        return [self.noun, 
                self.article,
                self.plural,
                self.translation, 
                self.status, 
                self.step, 
                self.ease, 
                str(self.next_review)]
    
    def create_time_from_string():
        pass