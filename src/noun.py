from datetime import datetime, timedelta

TIME_STRING_FORMAT = '%y-%m-%d %H:%M:%S.%f'

class Noun():
    def __init__(self, noun, article=None, plural=None, translation=None, status='learning', step=0, ease=2.5, next_review=datetime.now(), interval=timedelta(seconds=0)):
        self.article = article
        self.noun = noun
        self.plural = plural
        self.translation = translation
        self.status = status
        self.step = int(step)
        self.ease = max(float(ease), 1.3)
        self.next_review = self.convert_to_datetime(next_review)
        self.card_front = f'... {self.noun} - ({self.translation})'
        self.card_back = str(self)
        self.overdue = datetime.now() - self.next_review
        self.interval = self.convert_to_timedelta(interval)


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

    def convert_to_datetime(self, dt):
        if dt == '':
            return datetime.now()
        elif type(dt) == str:
            return datetime.strptime(dt, TIME_STRING_FORMAT)
        elif type(dt) == datetime:
            return dt
        else:
            raise Exception(f'Time type error for {self.noun}')
        
    # Format: 1 day, 0:00:01
    def convert_to_timedelta(self, interval):
        if interval == '':
            return timedelta(seconds=0)
        elif type(interval) == timedelta:
            return interval
        elif interval[2:5] == 'day' or interval[3:7] == 'days':
            days = int(interval.split(' ')[0])
            time = interval.split(', ')
            hours, minutes, seconds = time[1].split(':')
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)
            return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        else:
            time = interval.split(', ')
            hours, minutes, seconds = time[1].split(':')
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)
            return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        

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
        return [self.noun, self.article, self.plural, self.translation, self.status, self.step, self.ease, self.next_review.strftime(TIME_STRING_FORMAT), self.interval]
    
    def feedback(self, answer: str):
        answer_options = ['again', 'hard', 'good', 'easy']
        if self.status == 'learning':
            if answer == answer_options[0]: #again
                self.interval = timedelta(minutes=1)
                self.next_review = datetime.now() + self.interval
            elif answer == answer_options[1]: #hard
                self.interval = timedelta(minutes=6)
                self.next_review = datetime.now() + self.interval
                self.step = 1
            elif answer == answer_options[2]: #good
                if self.step == 0:
                    self.interval = timedelta(minutes=10)
                    self.next_review = datetime.now() + self.interval
                    self.step = 1
                elif self.step == 1:
                    self.status = 'reviewing'
                    self.interval = timedelta(days=1)
                    self.next_review = datetime.now() + self.interval
            elif answer == answer_options[3]: #easy
                self.status = 'reviewing'
                self.interval = timedelta(days=4)
                self.next_review = datetime.now() + self.interval

        elif self.status == 'reviewing':
            if answer == answer_options[0]: #again
                self.status = 'relearning'
                self.interval = timedelta(minutes=10)
                self.next_review = datetime.now() + self.interval
                self.ease -= 0.2
            elif answer == answer_options[1]: #hard
                self.status = 'reviewing'
                self.interval *= 1.2
                self.next_review = datetime.now() + self.interval
                self.ease -= 0.15
            elif answer == answer_options[2]: #good
                self.status = 'reviewing'
                self.interval *= self.ease
                self.next_review = datetime.now() + self.interval
            elif answer == answer_options[3]: #easy
                self.status = 'reviewing'
                self.interval *= self.ease * 1.5
                self.next_review = datetime.now() + self.interval
                self.ease += 0.15

        elif self.status == 'relearning':
            if answer == answer_options[0]: #again
                self.interval = timedelta(minutes=1)
                self.next_review = datetime.now() + self.interval
            elif answer == answer_options[1]: #hard
                self.interval = timedelta(minutes=6)
                self.next_review = datetime.now() + self.interval
            elif answer == answer_options[2]: #good
                self.status = 'reviewing'
                self.interval = timedelta(days=1)
                self.next_review = datetime.now() + self.interval
            elif answer == answer_options[3]: #easy
                self.status = 'reviewing'
                self.interval = timedelta(days=4)
                self.next_review = datetime.now() + self.interval


if __name__ == '__main__':
    print('Main is noun.py')
    noun = Noun('Arbeit')
    print(noun.interval)