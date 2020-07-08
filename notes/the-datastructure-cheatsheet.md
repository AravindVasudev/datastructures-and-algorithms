# The Datastructure Cheatsheet

This document is made with the intention to be quickly glanced before an
interview.

## Map

### Implementations

#### HashTable
- Java 7: HashMap
  - Hashtable.
  -  Collision Resolution: Separate Chaining using Linked List.
  -  [Documentation](https://docs.oracle.com/javase/7/docs/api/java/util/HashMap.html).
- Java 8: HashMap
  - Hashtable.
  - Collision Resolution: Separate Chaining using Linked List but switches to balanced tree after a threshold. [source](http://openjdk.java.net/jeps/180).
  - [Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html).
- Python 3: dict
  - Hashtable. [source](https://docs.python.org/3/faq/design.html#how-are-dictionaries-implemented-in-cpython).
  - Collision Resolution: Open Addressing (Quadratic Probing). [source](https://www.laurentluce.com/posts/python-dictionary-implementation/)
  - [Documentation](https://docs.python.org/3/library/stdtypes.html#dict).

The complexities are the same for all three.
| Operation | Average Case | Amortized Case |
| :-------: | :----------: | :------------: |
| Insertion |     O(1)     |      O(N)      |
| Retrieval |     O(1)     |      O(N)      |


## References
- [Python Time Complexities](https://wiki.python.org/moin/TimeComplexity).