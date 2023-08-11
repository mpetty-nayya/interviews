require_relative '../lib/cache'
require_relative '../lib/node'

describe Cache do
    it 'constructs' do
        cache = described_class.new(2)
        expect(cache.head).to be_nil
        expect(cache.tail).to be_nil
        expect(cache.current_size).to eq(0)
        expect(cache.max_size).to eq(2)
    end

    it 'returns nil when getting nil key' do
        cache = described_class.new(2)        
        result = cache.get(nil)
        expect(result).to be_nil
    end

    it "returns nil for non cached key" do
        cache = described_class.new(2)        
        result = cache.get('apples')
        expect(result).to be_nil
    end
    

    it 'does not support setting nil key' do
        cache = described_class.new(2)        
        cache.put(nil, '111')
        expect(cache.head).to be_nil
        expect(cache.tail).to be_nil
        expect(cache.current_size).to eq(0)
        expect(cache.max_size).to eq(2)
    end

    it "supports 1 cached value" do
        cache = described_class.new(3)
        cache.put('bananas', 111)       
        expect(cache.current_size).to eq(1)
        expect(cache.tail.value).to eq(111)
        expect(cache.head.value).to eq(111)
    end

    it "supports 2 cached values" do
        cache = described_class.new(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)        
        expect(cache.current_size).to eq(2)
        expect(cache.tail.value).to eq(222)
        expect(cache.head.value).to eq(111)
    end

    it 'enforces max size on set' do
        cache = described_class.new(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)
        cache.put('cucumbers', 444)                
        expect(cache.current_size).to eq(3)
        expect(cache.to_a).to eq([222, 333, 444])
    end

    it 'gets tail' do
        cache = described_class.new(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)        
        cache.get('oranges')
        expect(cache.to_a).to eq([111, 222, 333])
    end

    it 'gets head' do
        cache = described_class.new(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)        
        cache.get('bananas')
        expect(cache.to_a).to eq([222, 333, 111])
    end

    it 'moves tail when getting middle' do
        cache = described_class.new(3)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)        
        cache.get('apples')
        expect(cache.to_a).to eq([111, 333, 222])      
    end

    it 'moves tail on multiple gets' do
        cache = described_class.new(4)
        cache.put('bananas', 111)
        cache.put('apples', 222)
        cache.put('oranges', 333)
        cache.put('cucumbers', 444)
        cache.put('peaches', 555)
        cache.get('oranges')
        cache.get('apples')
        cache.get('cucumbers')
        expect(cache.to_a).to eq([555, 333, 222, 444])
    end
end
