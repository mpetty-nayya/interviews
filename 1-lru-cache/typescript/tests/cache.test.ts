import {describe, expect, test} from '@jest/globals';

import { Cache } from '../src/cache'

describe('Cache', () => {
    test('constructs', () => {
        const cache = new Cache(2)    
        expect(cache.head).toBeNull
        expect(cache.tail).toBeNull
        expect(cache.currentSize).toBe(0)        
        expect(cache.maxSize).toBe(2)
    });

    test('returns nil for non cached key', () => {
        const cache = new Cache(2)        
        const result = cache.get('apples')
        expect(result).toBeNull
    });

    test('supports 1 cached value', () => {
        const cache = new Cache(3)
        cache.put('bananas', 111)       
        expect(cache.currentSize).toBe(1)
        expect(cache.tail.value).toBe(111)
        expect(cache.head.value).toBe(111)
    });

    test('supports 2 cached values', () => {
        const cache = new Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)        
        expect(cache.currentSize).toBe(2)
        expect(cache.tail.value).toBe(222)
        expect(cache.head.value).toBe(111)
    });

    test('enforces max size on set', () => {
        const cache = new Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)
        cache.put('cucumbers', 444)                
        expect(cache.currentSize).toBe(3)
        expect(cache.toArray()).toEqual([222, 333, 444])
    });

    test('gets tail', () => {
        const cache = new Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)        
        cache.get('oranges')
        expect(cache.toArray()).toEqual([111, 222, 333])
    });

    test('gets head', () => {
        const cache = new Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)        
        cache.get('bananas')
        expect(cache.toArray()).toEqual([222, 333, 111])
    });

    test('moves tail when getting middle', () => {
        const cache = new Cache(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)        
        cache.get('apples')
        expect(cache.toArray()).toEqual([111, 333, 222])
    });

    test('moves tail on multiple gets', () => {
        const cache = new Cache(4)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)
        cache.put('cucumbers', 444)
        cache.put('peaches', 555)
        cache.get('oranges')
        cache.get('apples')
        cache.get('cucumbers')                
        expect(cache.toArray()).toEqual([555, 333, 222, 444])
    });
});
