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
        self.my_nested_dict = {
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
                },
                {
                    'd': {
                        'step': 'logout',
                        'url': 'https://example.com/logout'
                    },
                    'e': [
                        {
                            'step': 'profile',
                            'url': 'https://example.com/profile'
                        },
                        {
                            'step': 'feed',
                            'url': 'https://example.com/feed'
                        }

                    ]
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
        self.assertEqual(
            'https://example.com/other',
            get_adjacent_key(self.my_dict, 'step', ['buy', 'other'], 'url')
        )
        self.assertEqual(
            'https://example.com/enter',
            get_adjacent_key(self.my_dict, 'step', ['buy', 'enter', 'other'], 'url')
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
            None,
            get_adjacent_key(self.my_dict, 'url', 'https://example.com/buy', 'step')
        )

    @unittest.skip('Skip initially, enable if nested structures are handled')
    def test_nested_structures(self):
        self.assertEqual(
            'profile',
            get_adjacent_key(self.my_nested_dict, 'url', 'https://example.com/profile', 'step')
        )
        self.assertEqual(
            'https://example.com/feed',
            get_adjacent_key(self.my_nested_dict, 'step', 'feed', 'url')
        )


if __name__ == '__main__':
    unittest.main()
