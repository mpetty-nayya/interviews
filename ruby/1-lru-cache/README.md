# Overview

A Cache is a type of data structure that allows applications to store data temporarily (as key-value pairs).  Allowing for efficient retrieval of commonly accessed data

A Least Recently Used (LRU) Cache organizes data in order of use, allowing you to quickly identify which item hasn't been used for the longest amount of time.

# Goal

Fix the cache so all unit tests pass.  Note that unit tests are written correctly, the implemenation has a bug.


# Implementation

Our LRU Cache is implemented by pairing a Doubly Linked List with a ruby Hash

* **lib**  - dir containing implementation
* **spec** - dir containing unit tests
* [lru-cache.png](lur-cache.png) - diagrom of cache usage

# Run Tests

```bash
# execute rspec to run tests
rspec .
```

See [root readme](../README.md) to install ruby and rspec
