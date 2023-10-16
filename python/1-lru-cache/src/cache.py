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
        if self.tail is result: # if the tail item is the got item, no reordering necessary
            return result.value

        # REORDERING 
        if None == result.prevNode: # if the got item's prev is NONE, then it's the head
            self.head = result.nextNode # the got item becomes the head
            self.head.prevNode = None # the new head item now has no prevNode, since it's the head
        else: # it's not the head or tail, so it's a bit more tricky
            result.prevNode.nextNode = result.nextNode # replace the nextNode marker in the prev item to the result next node
            result.nextNode.prevNode = result.prevNode # replace the prevNode marker in the next item to the result prev node

        self.tail.nextNode = result # the old tail node's next becomes the result, moving result to the tail spot
        result.nextNode = None # the tail's next is None, because it's in hte tail spot
        result.prevNode = self.tail # move the old tail to the prev spot of the got item
        self.tail = result # denote the tail as the result value
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
