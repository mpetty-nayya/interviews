from src.methods import get_adjacent_key
import unittest

class MethodsTest(unittest.TestCase):

    def setUp(self):
        self.my_dict = {
            'a': {
                'step': 'authorize',
                'url': 'https://example.com/authorize'
            },
            'b': {
                'step': 'enter',
                'url': 'https://example.com/enter'
            },
            'c': [                                
                {
                    'step': 'exit',
                    'url': 'https://example.com/exit'
                },
                {
                    'step': 'other',
                    'url': 'https://example.com/other'
                }
            ]
        }

    def test_get_url_by_step(self):
        self.assertEqual(
            'https://example.com/authorize',
            get_adjacent_key(self.my_dict, 'step', 'authorize', 'url')
        )
        self.assertEqual(
            'https://example.com/exit',
            get_adjacent_key(self.my_dict, 'step', 'exit', 'url')
        )
        self.assertEqual(
            'https://example.com/enter',
            get_adjacent_key(self.my_dict, 'step', 'enter', 'url')
        )
        self.assertEqual(
            'https://example.com/other',
            get_adjacent_key(self.my_dict, 'step', 'other', 'url')
        )

    def test_get_step_by_url(self):
        self.assertEqual(
            'authorize',
            get_adjacent_key(self.my_dict, 'url', 'https://example.com/authorize', 'step')
        )
        self.assertEqual(
            'exit',
            get_adjacent_key(self.my_dict, 'url', 'https://example.com/exit', 'step')
        )
        self.assertEqual(
            'enter',
            get_adjacent_key(self.my_dict, 'url', 'https://example.com/enter', 'step')
        )
        self.assertEqual(
            'other',
            get_adjacent_key(self.my_dict, 'url', 'https://example.com/other', 'step')
        )

    def test_no_match(self):
        self.assertEqual(
            'authorize',
            get_adjacent_key(self.my_dict, 'url', 'https://example.com/authorize', 'step')
        )

if __name__ == '__main__':
    unittest.main()
