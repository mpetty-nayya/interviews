class Node
    attr_accessor :prev_node, :next_node, :value

    def initialize(value, prev_node, next_node)
        @value = value
        @next_node = next_node
        @prev_node = prev_node
    end
end
