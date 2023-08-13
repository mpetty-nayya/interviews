from src.node import Node

class Cache:
    def __init__(self, maxSize) -> None:
        self.head = None
        self.tail = None
        self.currentSize = 0
        self.maxSize = maxSize
        self.lookupTable = {}

    def get(self, key) -> int:
        if None == key:
            return None

        if key not in self.lookupTable.keys():
            return None

        result = self.lookupTable[key]        
        if self.tail is result:
            return result.value

        if None == result.prevNode:
            self.head = result.nextNode
            self.head.prevNode = None        

        self.tail.nextNode = result
        result.nextNode = None
        result.prevNode = None
        self.tail = result
        return result.value

    def put(self, key, val) -> None:
        if None == key:
            return None

        self.currentSize += 1
        if self.currentSize > self.maxSize:
            self.lookupTable.pop(self.head.key)
            self.head = self.head.nextNode
            self.head.prevNode = None
            self.currentSize -= 1
        
        newNode = Node(key, val, self.tail, None)
        if None == self.tail:
            self.head = newNode
        else:
            self.tail.nextNode = newNode
        
        self.tail = newNode
        self.lookupTable[key] = newNode
    
    def toArray(self):        
        a = []
        current = self.head
        while None != current:
            a.append(current.value)
            current = current.nextNode
        
        return a
