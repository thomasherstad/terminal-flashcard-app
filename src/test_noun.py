import unittest

from noun import Noun

class TestNoun(unittest.TestCase):
    def test_to_list_format_new_noun(self):
        data = Noun('Kraft', 'Die', 'Kräfte', 'Force')
        expected = ['Kraft', 'Die', 'Kräfte', 'Force', None, '0']
        output = data.to_list_format()
        self.assertEqual(output, expected)

    def test_to_list_format_used_noun(self):
        data = Noun('Kraft', 'Die', 'Kräfte', 'Force', '2024-07-29', '10')
        expected = ['Kraft', 'Die', 'Kräfte', 'Force', '2024-07-29', '10']
        output = data.to_list_format()
        self.assertEqual(output, expected)
    
    def test_to_list_format_minimum(self):
        data = Noun('Kraft')
        expected = ['Kraft', None, None, None, None, '0']
        output = data.to_list_format()
        self.assertEqual(output, expected)
    
    def test_str_new(self):
        noun = Noun('Kraft', 'Die', 'Kräfte', 'Force')
        expected = 'Die Kraft, Die Kräfte (Force)'
        output = str(noun)
        self.assertEqual(output, expected)

    def test_str_used(self):
        noun = Noun('Kraft', 'Die', 'Kräfte', 'Force', '2024-07-29', '10')
        expected = 'Die Kraft, Die Kräfte (Force)'
        output = str(noun)
        self.assertEqual(output, expected)

    def test_str_minimum(self):
        noun = Noun('Kraft')
        expected = 'Kraft - Missing Information'
        output = str(noun)
        self.assertEqual(output, expected)

    def test_eq_same(self):
        noun1 = Noun('Kraft', 'Die', 'Kräfte', 'Force')
        noun2 = Noun('Kraft', 'Die', 'Kräfte', 'Force')
        equal = (noun1 == noun2)
        self.assertTrue(equal)
        
    def test_eq_more_info(self):
        noun1 = Noun('Kraft', 'Die', 'Kräfte', 'Force')
        noun2 = Noun('Kraft', 'Die', 'Kräfte', 'Force', '2024-07-29', '15')
        self.assertTrue(noun1 == noun2)
    
    def test_eq_different(self):
        noun1 = Noun('Kraft', 'Die', 'Kräfte', 'Force')
        noun2 = Noun('Bahn', 'Die', 'Bahne', 'Train')
        self.assertFalse(noun1 == noun2)

    #TODO: Come up with better example
    def test_eq_different_translation(self):
        noun1 = Noun('Bahn', 'Die', 'Bahne', 'Rail')
        noun2 = Noun('Bahn', 'Die', 'Bahne', 'Train')
        self.assertFalse(noun1 == noun2)

    def test_eq_different_article(self):
        noun1 = Noun('See', 'Die', 'Seen', 'Ocean')
        noun2 = Noun('See', 'Der', 'Seen', 'Lake')
        self.assertFalse(noun1 == noun2)

    # test __lt__
    def test_lt_different_noun(self):
        noun1 = Noun('Bahn', 'Die', 'Bahne', 'Train')
        noun2 = Noun('See', 'Der', 'Seen', 'Lake')
        self.assertLess(noun1, noun2)
    
    #This is to make sure sorting behavior for different follows der, die, das
    def test_lt_different_article(self):
        noun1 = Noun('See', 'Die', 'Seen', 'Ocean')
        noun2 = Noun('See', 'Der', 'Seen', 'Lake')
        self.assertLess(noun2, noun1)

    # test get_article_from_user (might need rewrite to make testable)
    