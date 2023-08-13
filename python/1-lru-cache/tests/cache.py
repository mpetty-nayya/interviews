from src.cache import Cache
import unittest

class CachTest(unittest.TestCase):

    def test_constructs(self):
        cache = Cache(maxSize=3)
        self.assertIsNone(cache.head)
        self.assertIsNone(cache.tail)
        self.assertEqual(3, cache.maxSize)        
        self.assertEqual(0, cache.currentSize)

    def test_returns_nil_when_getting_nil_key(self):
        cache = Cache(2)        
        result = cache.get(key=None)
        self.assertIsNone(result)

    def test_supports_1_cached_value(self):
        cache = Cache(3)
        cache.put('bananas', 111)       
        self.assertEqual(cache.currentSize, 1)
        self.assertEqual(cache.tail.value, 111)
        self.assertEqual(cache.head.value, 111)
    
    def test_supports_2_cached_values(self):
        cache =Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)        
        self.assertEqual(cache.currentSize, 2)
        self.assertEqual(cache.tail.value, 222)
        self.assertEqual(cache.head.value, 111)

    def test_enforces_max_size_on_set(self):
        cache = Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)
        cache.put('cucumbers', 444)                
        self.assertEqual(cache.currentSize, 3)
        self.assertEqual(cache.toArray(), [222, 333, 444])
    
    def test_gets_tail(self):
        cache = Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)        
        cache.get('oranges')
        self.assertEqual(cache.toArray(), [111, 222, 333])
        
    def test_gets_head(self):
        cache = Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)        
        cache.get('bananas')
        self.assertEqual(cache.toArray(), [222, 333, 111])    
    
    def test_moves_tail_when_getting_middle(self):
        cache = Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)        
        cache.get('apples')
        self.assertEqual(cache.toArray(), [111, 333, 222])

    def test_moves_tail_on_multiple_gets(self):
        cache = Cache(4)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)
        cache.put('cucumbers', 444)
        cache.put('peaches', 555)
        cache.get('oranges')
        cache.get('apples')
        cache.get('cucumbers')                
        self.assertEqual(cache.toArray(), [555, 333, 222, 444])
    
if __name__ == '__main__':
    unittest.main()

