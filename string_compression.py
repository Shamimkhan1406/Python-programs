"""Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12"."""

def compress(chars):
    n = len(chars)
    if n == 0:
        return 1
    i,indx = 0,0
    while i<n:
        cur_char = chars[i]
        count = 0
        # Count the number of occurrences of the current character
        while i < n and chars[i] == cur_char:
            count += 1
            i += 1
        # Store the character
        chars[indx] = cur_char
        indx += 1
        # If count is greater than 1, store the count as well
        if count > 1:
            for digit in str(count):
                chars[indx] = digit
                indx += 1
    # Return the new length of the compressed array
    return indx
# Example usage:
if __name__ == "__main__":
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    new_length = compress(chars)
    print(new_length)  # Output: 6
    print(chars[:new_length])  # Output: ['a', '2', 'b', '2', 'c', '3']
    
    chars = ["a"]
    new_length = compress(chars)
    print(new_length)  # Output: 1
    print(chars[:new_length])  # Output: ['a']
    
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    new_length = compress(chars)
    print(new_length)  # Output: 4

#time Complexity: O(n), where n is the number of characters in the input array.
#Space Complexity: O(1), as we are using only a few extra variables.
#This code implements a character compression algorithm that modifies the input array in place.
#It iterates through the array, counting consecutive occurrences of each character.
#When a character changes, it stores the character and its count (if greater than 1) in the array.
#The algorithm efficiently compresses the characters without using additional space for storage,
#ensuring that the final result is stored in the original array.
#The approach is optimal for the problem and does not require any additional data structures,
#thus maintaining a constant space complexity.
#The algorithm handles cases where characters appear consecutively and compresses them into a single character followed
#by the count of occurrences, if applicable.
#The solution is efficient and works well for large inputs, ensuring that the input array is modified in place.
#The final length of the compressed array is returned, which can be used to access the compressed characters.
#The algorithm is designed to handle edge cases, such as single characters or characters that do not repeat,
#ensuring that the output is always valid and correctly formatted.
        