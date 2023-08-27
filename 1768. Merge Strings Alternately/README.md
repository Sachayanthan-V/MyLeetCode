## Description
Given two strings `word1` and `word2`, merge them into a single string by **alternating** the characters from each string. If one string is longer than the other, append the remaining characters to the end of the merged string.

## Example
Input: `word1` = "abc", `word2` = "pq"
Output: "apbqca"

## Implementation
Here is a `Python` implementation of the solution:

# Intuition
* $$O(n)$$ 
***n*** is the max length of either a String of word1 or word2

# Approach
- iterate over smaller length to elements append to external string
- adding remaining character if missed at last either word1 or word2 and return it

# Complexity
- Time complexity:
`O(n)` - 'n' is the max length of one of given string.

- Space complexity:
`O(1)` - storing, word1, word2 & newString variable. its eliminatable, So, O(1)

# Code
```
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        MergeString = '' 
        length = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range(length):
            MergeString += word1[i]
            MergeString += word2[i]
        if length < len(word1):
            MergeString += word1[length:]
        if length < len(word2):
            MergeString += word2[length:]
        return MergeString
```

## Step-by-Step Explanation
1. Initialize an empty string *`MergeString`* to store the merged string.
2. Find the length of the shorter string.
3. Iterate over the shorter string and append the characters from each string to *`MergeString`*, alternating between the two strings.
4. If one string is longer than the other, append the remaining characters to the end of *`MergeString`*.
5. Return the merged string.

## Conclusion
This solution uses a simple loop to iterate over the shorter string and append the characters from each string to the merged string. The code is easy to understand and implement.


## Author

- [SachayanthanV](https://github.com/johndoe) - Github , Author of [This Repository](https://github.com/Sachayanthan-V/MyLeetCode)

- [linkedIn - SachayanthanVJain](https://www.linkedin.com/in/sachayanthan-v-jain-040838150/) - Software Engineer