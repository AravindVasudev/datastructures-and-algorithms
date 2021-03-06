# The Datastructure Cheatsheet

This document is made with the intention to be quickly glanced before an
interview.

## Map

### Implementations

#### HashTable
- Java 7: `HashMap`
  - Hashtable.
  -  Collision Resolution: Separate Chaining using Linked List.
  -  [Documentation](https://docs.oracle.com/javase/7/docs/api/java/util/HashMap.html).
- Java 8: `HashMap`
  - Hashtable.
  - Collision Resolution: Separate Chaining using Linked List but switches to balanced tree after a threshold. [source](http://openjdk.java.net/jeps/180).
  - [Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html).
- Java: `HashTable`
  - Thread-Safe.
  - Does not allow null key or value (HashMap allows null key and value).
  - Legacy. Use [`ConcurrentHashMap`](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html) instead.
  - [Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/Hashtable.html).
- Python 3: `dict`
  - Hashtable. [source](https://docs.python.org/3/faq/design.html#how-are-dictionaries-implemented-in-cpython).
  - Collision Resolution: Open Addressing (Quadratic Probing). [source](https://www.laurentluce.com/posts/python-dictionary-implementation/)
  - [Documentation](https://docs.python.org/3/library/stdtypes.html#dict).
- Python 3: `collections.defaultdict`
  - Same as `dict` but when lookup fails, it creates the element with the default value.

The complexities are the same for all the cases above.
| Operation | Average Case | Amortized Case |
| :-------: | :----------: | :------------: |
| Insertion |     O(1)     |      O(N)      |
| Retrieval |     O(1)     |      O(N)      |

#### Ordered Map
- Java: `LinkedHashMap`
  - HashTable and Doubly Linked List.
  - Similar to LRU cache implementation.
  - Similar insertion & deletion complexity to HashMap.
  - iteration through the map: O(N).
  - [Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html).
- Python 3: `collections.OrderedDict`
  - HashTable and Doubly Linked List. [source code](https://github.com/python/cpython/blob/b26a0db8ea2de3a8a8e4b40e69fc8642c7d7cb68/Lib/collections/__init__.py#L94).
  - [Documentation](https://docs.python.org/3/library/collections.html#collections.OrderedDict)

The complexities are same as HashTable.

#### Sorted Map
- Java: `TreeMap`
  - Red-Black Tree.
  - Insertion & Retrieval: O(log N).
  - Use [ConcurrentSkipListMap](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentSkipListMap.html) for thread-safety.
  - [Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html).
  
Python 3 does not have sorted map implementation.

#### Array
- Custom
  - Can be used as map when keys are within a small range and hashable.
  - Lesser memory usage and better amortized case than HashTable.
  - Eg cases: characters, years, etc.
- Java: `EnumMap`
  - All keys come from enum.
  - Internally implemented as array.
  - Extremely compact and efficient.
  - [Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/EnumMap.html).

#### Misc
- Python 3: `collections.ChainMap`
  - Groups multiple dicts or other mappings together to create a single, updateable view.
  - Implemented as list.
  - [Documentation](https://docs.python.org/3/library/collections.html#collections.ChainMap).
- Python 3: `collections.Counter`
  - Stores count of hashed objects.
  - Bag datastructure.
  - [Documentation](https://docs.python.org/3/library/collections.html#collections.Counter).
  - Eg:

```python
>>> Counter('hello')
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
```


## References
- [Python Time Complexities](https://wiki.python.org/moin/TimeComplexity).