# Guide to Two-Pointer Techniques

## Table of Contents

1. [Introduction](#introduction)
2. [Pattern: Opposite Direction Pointers](#pattern-opposite-direction-pointers)
3. [Pattern: Same Direction Pointers](#pattern-same-direction-pointers)
4. [Pattern: Fast and Slow Pointers](#pattern-fast-and-slow-pointers)
5. [Pattern: Multiple Pointers](#pattern-multiple-pointers)
6. [Pattern: Greedy with Two Pointers](#pattern-greedy-with-two-pointers)
7. [Advanced Techniques](#advanced-techniques)

## Introduction

Two-pointer technique is a powerful pattern for solving array and string problems efficiently. It typically reduces the time complexity from O(n²) to O(n) by avoiding nested loops.

Key implementation patterns:

- Opposite direction (one at start, one at end)
- Same direction (both moving forward at different paces)
- Fast & slow pointers
- Multiple pointers (three or more)

## Pattern: Opposite Direction Pointers

### Problem: Valid Palindrome (125)

**Task**: Determine if a string is a palindrome, considering only alphanumeric characters and ignoring case.

**API**:

```python
def isPalindrome(s: str) -> bool
```

**Implementation**:

```python
def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### Problem: Container With Most Water (11)

**Task**: Find two lines that together with the x-axis form a container that holds the most water.

**API**:

```python
def maxArea(height: List[int]) -> int
```

**Implementation**:

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate current area
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)

        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### Problem: Reverse String (344)

**Task**: Reverse a string in-place.

**API**:

```python
def reverseString(s: List[str]) -> None
```

**Implementation**:

```python
def reverseString(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### Problem: Valid Palindrome II (680)

**Task**: Determine if a string can become a palindrome by removing at most one character.

**API**:

```python
def validPalindrome(s: str) -> bool
```

**Implementation**:

```python
def validPalindrome(s):
    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping left character or right character
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

## Pattern: Same Direction Pointers

### Problem: Remove Duplicates from Sorted Array (26)

**Task**: Remove duplicates from a sorted array in-place and return the new length.

**API**:

```python
def removeDuplicates(nums: List[int]) -> int
```

**Implementation**:

```python
def removeDuplicates(nums):
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### Problem: Merge Sorted Array (88)

**Task**: Merge two sorted arrays nums1 and nums2 into nums1 as one sorted array.

**API**:

```python
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None
```

**Implementation**:

```python
def merge(nums1, m, nums2, n):
    # Start from the end of both arrays
    p1 = m - 1  # Pointer for nums1
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for merged result

    # While both arrays have elements to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If nums2 still has elements, copy them to nums1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
```

**Time Complexity**: O(m + n)
**Space Complexity**: O(1)

### Problem: Merge Strings Alternately (1768)

**Task**: Merge two strings by alternating their characters.

**API**:

```python
def mergeAlternately(word1: str, word2: str) -> str
```

**Implementation**:

```python
def mergeAlternately(word1, word2):
    result = []
    i, j = 0, 0

    # Alternate characters until one string is exhausted
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1

    # Append remaining characters from either string
    result.append(word1[i:])
    result.append(word2[j:])

    return ''.join(result)
```

**Time Complexity**: O(max(m, n))
**Space Complexity**: O(m + n)

## Pattern: Fast and Slow Pointers

### Problem: Rotate Array (189)

**Task**: Rotate an array to the right by k steps.

**API**:

```python
def rotate(nums: List[int], k: int) -> None
```

**Implementation**:

```python
def rotate(nums, k):
    n = len(nums)
    k %= n  # Handle case where k > n

    # Reverse the entire array
    reverse(nums, 0, n - 1)
    # Reverse the first k elements
    reverse(nums, 0, k - 1)
    # Reverse the remaining elements
    reverse(nums, k, n - 1)

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

## Pattern: Multiple Pointers

### Problem: Two Sum II - Input Array Is Sorted (167)

**Task**: Find two numbers that add up to a specific target in a sorted array.

**API**:

```python
def twoSum(numbers: List[int], target: int) -> List[int]
```

**Implementation**:

```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        curr_sum = numbers[left] + numbers[right]

        if curr_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]  # No solution
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### Problem: 3Sum (15)

**Task**: Find all unique triplets in the array that sum to zero.

**API**:

```python
def threeSum(nums: List[int]) -> List[List[int]]
```

**Implementation**:

```python
def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result
```

**Time Complexity**: O(n²)
**Space Complexity**: O(1) excluding output

### Problem: 4Sum (18)

**Task**: Find all unique quadruplets in the array that sum to the target.

**API**:

```python
def fourSum(nums: List[int], target: int) -> List[List[int]]
```

**Implementation**:

```python
def fourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicates for the second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    # Found a quadruplet
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

    return result
```

**Time Complexity**: O(n³)
**Space Complexity**: O(1) excluding output

## Pattern: Greedy with Two Pointers

### Problem: Boats to Save People (881)

**Task**: Return the minimum number of boats to carry every person, given a weight limit per boat.

**API**:

```python
def numRescueBoats(people: List[int], limit: int) -> int
```

**Implementation**:

```python
def numRescueBoats(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        # Try to pair heaviest with lightest
        if people[left] + people[right] <= limit:
            left += 1
        # If not possible, heaviest goes alone
        right -= 1
        boats += 1

    return boats
```

**Time Complexity**: O(n log n) due to sorting
**Space Complexity**: O(1)

## Advanced Techniques

### Problem: Trapping Rain Water (42)

**Task**: Compute how much water can be trapped after raining.

**API**:

```python
def trap(height: List[int]) -> int
```

**Implementation**:

```python
def trap(height):
    if not height or len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0

    while left < right:
        # Update max heights
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        # Calculate trapped water based on the smaller boundary
        if left_max < right_max:
            water += left_max - height[left]
            left += 1
        else:
            water += right_max - height[right]
            right -= 1

    return water
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### Optimization Techniques

1. **Pre-sorting**: Many two-pointer solutions require a sorted array

   - Example: 3Sum, 4Sum, Boats to Save People

2. **Skipping duplicates**: Critical for problems requiring unique solutions

   - Example: 3Sum skips repeated values to avoid duplicate triplets

3. **Bidirectional iteration**: Helps when you need O(1) space complexity

   - Example: Reverse String, Valid Palindrome

4. **In-place modification**: For problems that require modifying the input

   - Example: Remove Duplicates, Merge Sorted Array

5. **State tracking**: Keeping track of important values like max/min
   - Example: Trapping Rain Water's height tracking

## Common Pitfalls and Tips

1. **Edge cases**: Always consider:

   - Empty inputs
   - Single-element inputs
   - Inputs where pointers may not cross

2. **Boundary conditions**:
   - Be careful with array indexing
   - Check boundary conditions in while loops
   - Handle cases where pointers might be equal
3. **Optimization**:

   - Early termination when possible
   - Skip unnecessary iterations (e.g., duplicates)
   - Consider sorting when beneficial

4. **Implementation tips**:
   - Use descriptive variable names for pointers (e.g., `left`, `right` instead of `i`, `j`)
   - Add comments for tricky logic
   - Break complex logic into helper functions
