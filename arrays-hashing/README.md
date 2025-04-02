# Guide to Arrays and Hashing

## Table of Contents

1. [Introduction](#introduction)
2. [Core Array Operations](#core-array-operations)
3. [Hashing Fundamentals](#hashing-fundamentals)
4. [Pattern: Frequency Counting](#pattern-frequency-counting)
5. [Pattern: Two Pointers](#pattern-two-pointers)
6. [Pattern: Sliding Window](#pattern-sliding-window)
7. [Pattern: Prefix Sums](#pattern-prefix-sums)
8. [Pattern: Hash Map as Cache](#pattern-hash-map-as-cache)
9. [Data Structure Implementations](#data-structure-implementations)
10. [Advanced Techniques](#advanced-techniques)

## Introduction

Arrays and hash tables are fundamental data structures that form the basis for solving numerous algorithmic problems. This guide focuses on practical implementations and common patterns rather than theory.

Time complexity reference:

- Array access: O(1)
- Array search: O(n)
- Hash table insert/delete/search: O(1) average, O(n) worst case

## Core Array Operations

### Problem: Two Sum (1)

**Task**: Find two numbers in an array that add up to a specific target.

**Solution**: Use a hash map to store values and their indices.

```python
def twoSum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**Time Complexity**: O(n)
**Space Complexity**: O(n)

### Problem: Product of Array Except Self (238)

**Task**: Return an array where each element is the product of all array elements except the current one, without using division.

**Key Insight**: Use prefix and postfix products.

```python
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Calculate postfix products and multiply with prefix products
    postfix = 1
    for i in range(n-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result
```

**Time Complexity**: O(n)
**Space Complexity**: O(1) (excluding output array)

### Problem: Remove Element (27)

**Task**: Remove all occurrences of a value from an array in-place.

**Solution**: Two-pointer approach.

```python
def removeElement(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

## Hashing Fundamentals

### Problem: Contains Duplicate (217)

**Task**: Determine if an array contains any duplicate values.

**Solution**: Use a hash set to track seen values.

```python
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Time Complexity**: O(n)
**Space Complexity**: O(n)

### Problem: Valid Anagram (242)

**Task**: Determine if one string is an anagram of another.

**Solution**: Compare character frequencies using a hash map.

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}

    # Count characters in s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrement counts for characters in t
    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True
```

**Time Complexity**: O(n)
**Space Complexity**: O(k) where k is the size of the character set

### Problem: Group Anagrams (49)

**Task**: Group strings that are anagrams of each other.

**Solution**: Use sorted strings as hash map keys.

```python
def groupAnagrams(strs):
    anagram_groups = {}

    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(s)

    return list(anagram_groups.values())
```

**Alternative Solution**: Use character counts as tuple keys for better performance.

```python
def groupAnagrams(strs):
    anagram_groups = {}

    for s in strs:
        # Create count array for 26 lowercase letters
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1

        # Use tuple as key since lists can't be keys
        key = tuple(count)
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(s)

    return list(anagram_groups.values())
```

**Time Complexity**: $O(n \times k)$ where k is the maximum length of any string
**Space Complexity**: $O(n \times k)$

## Pattern: Frequency Counting

### Problem: Majority Element (169)

**Task**: Find the element that appears more than n/2 times in an array.

**Solution**: Use a hash map to count frequencies.

```python
def majorityElement(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num
    return -1  # No majority element exists
```

**Optimized Solution**: Boyer-Moore Voting Algorithm

```python
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        count += 1 if num == candidate else -1

    return candidate
```

**Time Complexity**: O(n)
**Space Complexity**: O(1) for optimized solution

### Problem: Majority Element II (229)

**Task**: Find all elements that appear more than n/3 times in an array.

**Solution**: Extended Boyer-Moore Voting Algorithm.

```python
def majorityElement(nums):
    if not nums:
        return []

    # At most 2 majority elements
    count1, count2 = 0, 0
    candidate1, candidate2 = None, None

    # First pass: find potential candidates
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Second pass: count actual occurrences
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### Problem: Top K Frequent Elements (347)

**Task**: Find the k most frequent elements in an array.

**Solution**: Use hash map and bucket sort.

```python
def topKFrequent(nums, k):
    # Count frequencies
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Create frequency buckets
    freq_buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        freq_buckets[freq].append(num)

    # Get top k elements
    result = []
    for i in range(len(freq_buckets) - 1, 0, -1):
        for num in freq_buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result  # Should never reach here if k is valid
```

**Time Complexity**: O(n)
**Space Complexity**: O(n)

## Pattern: Two Pointers

### Problem: Sort Colors (75)

**Task**: Sort an array containing only 0s, 1s, and 2s (Dutch National Flag problem).

**Solution**: Three-pointer approach.

```python
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

## Pattern: Sliding Window

### Problem: Best Time to Buy and Sell Stock II (122)

**Task**: Find maximum profit by buying and selling stocks multiple times.

**Solution**: Greedy approach to capture every upward trend.

```python
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

## Pattern: Prefix Sums

### Problem: Subarray Sum Equals K (560)

**Task**: Find the number of subarrays with sum equal to k.

**Solution**: Use prefix sums and a hash map.

```python
def subarraySum(nums, k):
    count = 0
    curr_sum = 0
    prefix_sums = {0: 1}  # Initialize with 0 sum occurring once

    for num in nums:
        curr_sum += num
        # If (curr_sum - k) exists in prefix_sums, it means
        # there's a subarray ending at the current position with sum k
        if curr_sum - k in prefix_sums:
            count += prefix_sums[curr_sum - k]

        # Update prefix_sums
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

    return count
```

**Time Complexity**: O(n)
**Space Complexity**: O(n)

### Problem: Range Sum Query 2D - Immutable (304)

**Task**: Efficiently query the sum of elements in a rectangle.

**Solution**: Precompute 2D prefix sums.

```python
class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        # Compute prefix sums
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix_sum[i][j] = (
                    self.prefix_sum[i-1][j] +
                    self.prefix_sum[i][j-1] -
                    self.prefix_sum[i-1][j-1] +
                    matrix[i-1][j-1]
                )

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.prefix_sum[row2+1][col2+1] -
            self.prefix_sum[row2+1][col1] -
            self.prefix_sum[row1][col2+1] +
            self.prefix_sum[row1][col1]
        )
```

**Time Complexity**: O(1) for queries, O(m*n) for initialization
**Space Complexity**: O(m*n)

## Pattern: Hash Map as Cache

### Problem: Longest Consecutive Sequence (128)

**Task**: Find the length of the longest consecutive elements sequence.

**Solution**: Use a hash set for O(1) lookups.

```python
def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting sequences from the smallest element
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count consecutive elements
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length
```

**Time Complexity**: O(n)
**Space Complexity**: O(n)

## Data Structure Implementations

### Problem: Design HashSet (705)

**Task**: Implement a HashSet without using built-in hash table libraries.

**Solution**: Array of linked lists (chaining).

```python
class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        hash_key = self._hash(key)
        if key not in self.buckets[hash_key]:
            self.buckets[hash_key].append(key)

    def remove(self, key):
        hash_key = self._hash(key)
        if key in self.buckets[hash_key]:
            self.buckets[hash_key].remove(key)

    def contains(self, key):
        hash_key = self._hash(key)
        return key in self.buckets[hash_key]
```

**Time Complexity**: O(1) average, O(n) worst case
**Space Complexity**: O(n)

### Problem: Design HashMap (706)

**Task**: Implement a HashMap without using built-in hash table libraries.

**Solution**: Array of linked lists with key-value pairs.

```python
class MyHashMap:
    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                self.buckets[hash_key][i] = (key, value)
                return
        self.buckets[hash_key].append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        for k, v in self.buckets[hash_key]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                del self.buckets[hash_key][i]
                return
```

**Time Complexity**: O(1) average, O(n) worst case
**Space Complexity**: O(n)

## Advanced Techniques

### Problem: First Missing Positive (41)

**Task**: Find the smallest missing positive integer in an array.

**Solution**: Use array indexing as a hash table.

```python
def firstMissingPositive(nums):
    n = len(nums)

    # Step 1: Mark numbers <= 0 or > n as n+1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    # Step 2: Mark indices corresponding to numbers in the array
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    # Step 3: Find the first positive number
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    # If all are negative, the answer is n+1
    return n + 1
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### Problem: Valid Sudoku (36)

**Task**: Determine if a 9x9 Sudoku board is valid.

**Solution**: Use hash sets to check rows, columns, and boxes.

```python
def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue

            num = board[i][j]
            box_idx = (i // 3) * 3 + j // 3

            # Check if number exists in row, column, or box
            if (num in rows[i] or num in cols[j] or num in boxes[box_idx]):
                return False

            # Add number to row, column, and box
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_idx].add(num)

    return True
```

**Time Complexity**: O(1) - since the board size is fixed
**Space Complexity**: O(1)

### Problem: Encode and Decode Strings (271)

**Task**: Design an algorithm to encode and decode a list of strings.

**Solution**: Use length prefixing with delimiters.

```python
class Codec:
    def encode(self, strs):
        # Format: [length]#[string][length]#[string]...
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            # Find the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1

            # Get the length
            length = int(s[i:j])

            # Get the string
            result.append(s[j+1:j+1+length])

            # Move index to the next string
            i = j + 1 + length

        return result
```

**Time Complexity**: O(n) for both encode and decode
**Space Complexity**: O(n)

### Problem: Sort an Array (912)

**Task**: Sort an array of integers.

**Solution**: Quick Sort implementation.

```python
def sortArray(nums):
    def quickSort(arr, low, high):
        if low < high:
            # Partition the array
            pivot_index = partition(arr, low, high)

            # Sort the partitions
            quickSort(arr, low, pivot_index - 1)
            quickSort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        # Choose rightmost element as pivot
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Place pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Call quickSort
    quickSort(nums, 0, len(nums) - 1)
    return nums
```

**Time Complexity**: O(n log n) average, O(n²) worst case
**Space Complexity**: O(log n) for recursion stack
