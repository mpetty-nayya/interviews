'use strict'

class Cache {
    constructor(maxSize) {
        this.tail = null
        this.head = null
        this.currentSize = 0
        this.maxSize = maxSize
        this.lookupTable = {}
    }

    get(key) {
        if (null === key) {
            return null
        }
        
        if (null == this.lookupTable[key]) {
            return null
        }
        
        const result = this.lookupTable[key]
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

    put(key, val) {
        if (null === key) {
            return null
        }

        this.currentSize += 1
        if (this.currentSize > this.maxSize) {
            delete this.lookupTable[this.head.key]
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
        this.lookupTable[key] = newNode
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

module.exports = Cache
