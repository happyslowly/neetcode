# Arrays and Hashing - Data Structures & Algorithms Reference Guide

## 1. API Interface

### Arrays
```python
# Core Operations
array[i]              # Access element at index i - O(1) time
array[i] = value      # Set element at index i - O(1) time
len(array)            # Get array length - O(1) time
array.append(value)   # Add element to end - O(1) amortized time
array.pop()           # Remove last element - O(1) time
array.insert(i, value)# Insert at index i - O(n) time
array.remove(value)   # Remove first occurrence - O(n) time
array.index(value)    # Find index of value - O(n) time
array[start:end]      # Slice array - O(end-start) time and space
```

### Hash Tables (Dictionaries in Python)
```python
# Core Operations
hash_table[key]       # Access value by key - O(1) average time
hash_table[key] = val # Set value for key - O(1) average time
key in hash_table     # Check if key exists - O(1) average time
hash_table.pop(key)   # Remove key-value pair - O(1) average time
hash_table.keys()     # Get view of all keys - O(1) time
hash_table.values()   # Get view of all values - O(1) time
hash_table.items()    # Get view of all key-value pairs - O(1) time
len(hash_table)       # Get number of entries - O(1) time
```

### Sets in Python
```python
# Core Operations
set.add(elem)         # Add element - O(1) average time
set.remove(elem)      # Remove element - O(1) average time
elem in set           # Check if element exists - O(1) average time
set1 & set2           # Intersection - O(min(len(s1), len(s2))) time
set1 | set2           # Union - O(len(s1) + len(s2)) time
set1 - set2           # Difference - O(len(s1)) time
len(set)              # Get number of elements - O(1) time
```

## 2. Implementation Details

### Arrays
- Contiguous memory allocation for fast random access
- Fixed size in many languages (dynamic in Python)
- Insertion/deletion in middle requires shifting elements
- Python lists are dynamic arrays with resizing strategies
- Memory overhead: Python lists add extra space for growth

### Hash Tables
- Key-value pairs with O(1) average access time
- Implemented using array of buckets + hash function
- Collision resolution via chaining or open addressing
- Load factor affects performance (items/buckets ratio)
- Python dictionaries use open addressing with probing
- Memory overhead: typically higher than arrays

### Common Operations Complexity
| Operation | Array | Hash Table | Set |
|-----------|-------|------------|-----|
| Access    | O(1)  | O(1) avg   | N/A |
| Search    | O(n)  | O(1) avg   | O(1) avg |
| Insert    | O(n)  | O(1) avg   | O(1) avg |
| Delete    | O(n)  | O(1) avg   | O(1) avg |
| Iterate   | O(n)  | O(n)       | O(n) |

## 3. Core Problem Patterns

### Two Sum Pattern (Find Pairs)
```python
def twoSum(nums, target):
    # Time: O(n), Space: O(n)
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # No solution found
```

### Frequency Counter Pattern
```python
def isAnagram(s, t):
    # Time: O(n), Space: O(1) - characters are limited
    if len(s) != len(t):
        return False
    
    # Count occurrences of each character
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True
```

### Set for Uniqueness/Existence
```python
def containsDuplicate(nums):
    # Time: O(n), Space: O(n)
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False
```

### Prefix Sum Pattern
```python
def productExceptSelf(nums):
    # Time: O(n), Space: O(1) (excluding output array)
    n = len(nums)
    output = [1] * n
    
    # Calculate products to the left of each element
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]
    
    # Multiply by products to the right of each element
    right_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output
```

### Running Sum with Hash Table
```python
def subarraySum(nums, k):
    # Time: O(n), Space: O(n)
    count = 0
    curr_sum = 0
    sum_counts = {0: 1}  # Empty subarray has sum 0
    
    for num in nums:
        curr_sum += num
        
        # If curr_sum - k exists, we have subarrays ending at current index
        if curr_sum - k in sum_counts:
            count += sum_counts[curr_sum - k]
        
        # Update running sum frequency
        sum_counts[curr_sum] = sum_counts.get(curr_sum, 0) + 1
    
    return count
```

## 4. Complete Solutions for Common Problems

### Two Sum (LeetCode #1)
```python
def twoSum(nums, target):
    # Time: O(n), Space: O(n)
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # No solution found
```

### Contains Duplicate (LeetCode #217)
```python
def containsDuplicate(nums):
    # Time: O(n), Space: O(n)
    return len(nums) != len(set(nums))
```

### Valid Anagram (LeetCode #242)
```python
def isAnagram(s, t):
    # Time: O(n), Space: O(1) - characters are limited
    if len(s) != len(t):
        return False
    
    # Option 1: Use Counter from collections
    from collections import Counter
    return Counter(s) == Counter(t)
    
    # Option 2: Manual counting
    """
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True
    """
```

### Group Anagrams (LeetCode #49)
```python
def groupAnagrams(strs):
    # Time: O(n * k log k), Space: O(n * k)
    # where n is length of strs and k is max string length
    anagram_groups = {}
    
    for s in strs:
        # Sort string to get canonical form for all anagrams
        key = ''.join(sorted(s))
        
        if key not in anagram_groups:
            anagram_groups[key] = []
        
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())
    
    # Optimization for large datasets:
    """
    from collections import defaultdict
    
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Use character counts as key - O(k) instead of O(k log k)
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        anagram_groups[tuple(counts)].append(s)
    
    return list(anagram_groups.values())
    """
```

### Top K Frequent Elements (LeetCode #347)
```python
def topKFrequent(nums, k):
    # Time: O(n) using bucket sort, Space: O(n)
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Create list of buckets for each frequency
    freq_buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        freq_buckets[freq].append(num)
    
    # Gather top k elements
    result = []
    for i in range(len(freq_buckets) - 1, 0, -1):
        result.extend(freq_buckets[i])
        if len(result) >= k:
            return result[:k]
    
    return result  # Should never reach here if k is valid
```

### Product of Array Except Self (LeetCode #238)
```python
def productExceptSelf(nums):
    # Time: O(n), Space: O(1) (excluding output array)
    n = len(nums)
    output = [1] * n
    
    # Calculate products to the left of each element
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]
    
    # Multiply by products to the right of each element
    right_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output
```

### Valid Sudoku (LeetCode #36)
```python
def isValidSudoku(board):
    # Time: O(9²), Space: O(9²)
    
    # Initialize sets to track seen digits
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            # Skip empty cells
            if val == '.':
                continue
                
            # Calculate box index (0-8)
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Check if digit already exists in row, column, or box
            if (val in rows[r] or
                val in cols[c] or
                val in boxes[box_idx]):
                return False
            
            # Mark digit as seen
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
    
    return True
```

### Longest Consecutive Sequence (LeetCode #128)
```python
def longestConsecutive(nums):
    # Time: O(n), Space: O(n)
    if not nums:
        return 0
    
    # Add all numbers to a set for O(1) lookups
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting sequences at the smallest number
        # This ensures each sequence is only counted once
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Count consecutive numbers in sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            max_length = max(max_length, current_streak)
    
    return max_length
```

### First Missing Positive (LeetCode #41)
```python
def firstMissingPositive(nums):
    # Time: O(n), Space: O(1)
    n = len(nums)
    
    # Step 1: Mark numbers <= 0 or > n as n+1
    # (they cannot be the answer and serve as markers)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Step 2: Use array indices as hash table
    # Mark presence of each number by negating nums[num-1]
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            # Mark as seen by making value negative
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find first missing positive
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    # If all numbers from 1 to n are present, return n+1
    return n + 1
```

### Design HashMap (LeetCode #706)
```python
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        # Time: O(1), Space: O(capacity)
        self.capacity = 1000  # Number of buckets
        self.buckets = [None] * self.capacity
    
    def _hash(self, key):
        # Simple hash function: key % capacity
        return key % self.capacity
    
    def put(self, key, value):
        # Time: O(1) average, O(n) worst case, Space: O(1)
        index = self._hash(key)
        
        # If bucket is empty, create new node
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
            return
        
        # Handle collision with linked list
        curr = self.buckets[index]
        prev = None
        
        # Check if key already exists
        while curr:
            if curr.key == key:
                curr.value = value  # Update existing key
                return
            prev = curr
            curr = curr.next
        
        # Add new key-value pair to the end of list
        prev.next = ListNode(key, value)
    
    def get(self, key):
        # Time: O(1) average, O(n) worst case, Space: O(1)
        index = self._hash(key)
        
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1  # Key not found
    
    def remove(self, key):
        # Time: O(1) average, O(n) worst case, Space: O(1)
        index = self._hash(key)
        
        curr = self.buckets[index]
        if not curr:
            return
        
        # If key is at the head of list
        if curr.key == key:
            self.buckets[index] = curr.next
            return
        
        # Check rest of the list
        prev = curr
        curr = curr.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

# Usage:
# hashMap = MyHashMap()
# hashMap.put(1, 1)
# hashMap.put(2, 2)
# hashMap.get(1)  # returns 1
# hashMap.get(3)  # returns -1
# hashMap.remove(2)
```

## 5. Common Pitfalls & Optimization Techniques

### Array Optimization
- Prefer in-place operations to avoid copying
- Use pre-allocated arrays