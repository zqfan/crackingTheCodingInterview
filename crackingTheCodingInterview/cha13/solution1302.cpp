/*
  Compare and contrast a hash table vs. an STL map. How is a hash table implemented?
If the number of inputs is small, what data structure options can be used instead of
a hash table?

Analyze:
# hash table vs stl map
* hash using hash function while map using key-value pair
* hash function need input can be hashed
* hash has waste memory space to reduce collision
* hash table is O(1) while map is O(logn)
* map can quickly get min or max value
* map can keep elements in sorted order

# hash table implementation
* a good hash function can spread hashed key uniformly
* a good collision resolving methods, such as chaining
* increasing or decreasing hash table size while input size is changed

# small inputs data structure
i'll use stl map, since n is small, O(logn) will slightly less than
O(1)
*/
