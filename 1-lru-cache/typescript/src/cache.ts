import { Node } from './node'

class Cache {
    readonly maxSize: number
    readonly lookupTable: Map<string, Node>
    currentSize: number;    
    head: Node
    tail: Node

    constructor(maxSize: number) {
        this.tail = null
        this.head = null
        this.currentSize = 0
        this.maxSize = maxSize
        this.lookupTable = new Map<string, Node>()
    }

    get(key: string): number {
        if (null === key) {
            return null
        }
        
        if (!this.lookupTable.has(key)) {
            return null
        }
        
        const result = this.lookupTable.get(key)
        if (this.tail === result) {
            return result.value
        }

        if (null === result.prevNode) {
            this.head = result.nextNode
            this.head.prevNode = null        
        }
        
        this.tail.nextNode = result
        result.nextNode = null
        result.prevNode = this.tail
        this.tail = result
        
        return result.value
    }

    put(key: string, val: number) {
        if (null === key) {
            return null
        }

        this.currentSize += 1
        if (this.currentSize > this.maxSize) {
            this.lookupTable.delete(this.head.key)
            this.head = this.head.nextNode
            this.head.prevNode = null
            this.currentSize -= 1
        }

        const newNode = {
            key: key, 
            value: val, 
            prevNode: this.tail,
            nextNode: null
        }

        if (null === this.tail) {
            this.head = newNode
        } else {
            this.tail.nextNode = newNode
        }        
        this.tail = newNode
        this.lookupTable.set(key, newNode)
    }

    toArray() {         
        const a = []
        var current = this.head
        while (null != current) {
            a.push(current.value)            
            current = current.nextNode            
        }               
        return a
    }
}

export { Cache }
