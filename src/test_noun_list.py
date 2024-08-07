import unittest

from noun_list import NounList, Noun

class TestNoun(unittest.TestCase):
    def create_case(self) -> NounList:
        noun1 = Noun('Kraft', 'Die', 'Kräfte', 'Force')
        noun2 = Noun('See', 'Der', 'Seen', 'Lake')
        noun3 = Noun('See', 'Die', 'Seen', 'Ocean')
        noun4 = Noun('Baum', 'Der', 'Bäume', 'Tree')
        test_nouns = NounList([noun1, noun2, noun3, noun4])
        return test_nouns

    def test_eq(self):
        nouns1 = self.create_case()
        nouns2 = self.create_case()
        equal = (nouns1 == nouns2)
        self.assertTrue(equal)

    def test_search_word_simple(self):
        word = 'Kraft'
        output = self.create_case()
        output = output.search_word(word)
        expected = NounList([Noun('Kraft', 'Die', 'Kräfte', 'Force')])
        self.assertTrue(output == expected)

    def test_search_word_two_matches(self):
        word = 'See'
        test_nouns = self.create_case()
        output = test_nouns.search_word(word)
        expected = NounList([Noun('See', 'Der', 'Seen', 'Lake'), Noun('See', 'Die', 'Seen', 'Ocean')])
        self.assertTrue(output == expected)

    def test_search_word_no_matches(self):
        word = 'Unternehmen'
        output = self.create_case()
        output = output.search_word(word)
        expected = NounList([])
        self.assertTrue(output == expected)