require_relative './node'

class Cache
    attr_accessor :head, :tail, :current_size, :max_size

    def initialize(max_size)
        @head = nil
        @tail = nil
        @current_size = 0
        @max_size = max_size
        @lookup_table = {}
    end
    
    def get(key)
        return nil if key.nil?
        result = @lookup_table[key]
        return nil unless result        
        return result.value if @tail == result
        if result.prev_node == nil
            @head = result.next_node
            @head.prev_node = nil        
        end        
        @tail.next_node = result
        result.next_node = nil
        result.prev_node = @tail
        @tail = result
        result.value
    end
    
    def put(key, val)
        return nil if key.nil?             
        @current_size += 1        
        if @current_size > @max_size         
            @lookup_table.delete(@lookup_table.key(@head))      
            @head = @head.next_node 
            @head.prev_node = nil
            @current_size -= 1
        end
        new_node = Node.new(val, @tail, nil)
        if @tail == nil 
            @head = new_node
        else
            @tail.next_node = new_node
        end
        @tail = new_node
        @lookup_table[key] = new_node
    end

    def to_a
        a = []
        current = @head
        while (current != nil)
            a.push(current.value)            
            current = current.next_node            
        end   
        a
    end
end
