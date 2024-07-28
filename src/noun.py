class Noun():
    def __init__(self, noun, article=None, plural=None, translation=None):
        self.article = article
        self.noun = noun
        self.plural = plural
        self.translation = translation
        self.date_last_correct = ''
        self.correct_streak = 0
    
    def __repr__(self):
        if self.translation and self.plural and self.article:
            return f'{self.article} {self.noun}, Die {self.plural} ({self.translation})'
        elif self.plural and self.article:
            return f'{self.article} {self.noun}, Die {self.plural}'
        else:
            return f'{self.article} {self.noun}'
            

    def get_article_from_user(self):
        articles = ['Der', 'Die', 'Das']
        while True:
            print(f'Which article does {self.noun} have?')
            answer = int(input('1.Der\t 2.Die\t 3.Das\n'))
            if answer in [1, 2, 3]:
                break
        self.article = articles[answer - 1]

    def get_plural_from_user(self):
        self.plural = input(f'What is the plural of {self.noun}?\n')

    def get_translation_from_user(self):
        self.translation = input(f'What does {self.noun} mean?\n')
        
        