# Overview

Based on the value of a specified key, I want to be able to extract the adjacent key's value. For instance - I want to find the value of “url” where the step's value is “exit”. 

```
{
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
```
# Goal

Implement the provided method so all unit test pass

See [root readme](../../README.md) to install python

# Running tests
```
interviews % cd 2-adjacent-key/python
python % python -m unittest tests.methods
```
