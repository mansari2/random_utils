"""
Python Patterns for Iterating and String Manipulations

This file demonstrates common techniques for iterating over data structures
and performing various string manipulation operations.
"""

import re

# -----------------------------
# Iteration Patterns
# -----------------------------

# 1. Iterating over a list with enumerate
def iterate_list(lst):
    for index, value in enumerate(lst):
        print(f"Index: {index}, Value: {value}")

# 2. Using a list comprehension to transform a list (e.g., squaring numbers)
def square_numbers(numbers):
    return [n ** 2 for n in numbers]

# 3. Iterating over a dictionary's items
def iterate_dictionary(d):
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

# 4. Iterating over two lists in parallel using zip
def iterate_zip(list1, list2):
    for item1, item2 in zip(list1, list2):
        print(f"List1 item: {item1}, List2 item: {item2}")

# 5. Using a generator expression to lazily compute squares
def generator_squares(numbers):
    return (n ** 2 for n in numbers)

# 6. Iterating with a while loop
def iterate_while(limit):
    count = 0
    while count < limit:
        print(f"Count: {count}")
        count += 1

# -----------------------------
# String Manipulation Patterns
# -----------------------------

# 7. Reversing a string using slicing
def reverse_string(s):
    return s[::-1]

# 8. Splitting a string into parts and then joining with a different delimiter
def split_and_join(s, delimiter=" "):
    parts = s.split(delimiter)
    joined = "-".join(parts)
    return parts, joined

# 9. Changing the case of a string
def change_case(s):
    return {
        "upper": s.upper(),
        "lower": s.lower(),
        "title": s.title(),
        "swapcase": s.swapcase()
    }

# 10. Replacing substrings within a string
def replace_substring(s, old, new):
    return s.replace(old, new)

# 11. Stripping leading and trailing whitespace from a string
def strip_whitespace(s):
    return s.strip()

# 12. Finding a substring within a string
def find_substring(s, substring):
    return s.find(substring)

# 13. Using regular expressions to find all matches of a pattern in a string
def regex_find(pattern, s):
    matches = re.findall(pattern, s)
    return matches

# 14. Iterating over each line in a multi-line string
def iterate_lines(multiline_str):
    for line in multiline_str.splitlines():
        print(line)

# 15. Iterating over words in a sentence
def iterate_words(sentence):
    words = sentence.split()
    for word in words:
        print(word)

# -----------------------------
# Example Usage
# -----------------------------

if __name__ == "__main__":
    # Iteration examples
    print("Iterating over list:")
    iterate_list([10, 20, 30, 40, 50])
    
    print("\nSquare numbers using list comprehension:")
    print(square_numbers([1, 2, 3, 4, 5]))
    
    print("\nIterating over dictionary:")
    iterate_dictionary({"apple": 3, "banana": 5, "cherry": 2})
    
    print("\nIterating with zip:")
    iterate_zip([1, 2, 3], ["one", "two", "three"])
    
    print("\nGenerator expression for squares:")
    gen = generator_squares([1, 2, 3, 4, 5])
    for value in gen:
        print(value)
    
    print("\nIterating with while loop:")
    iterate_while(5)
    
    # String manipulation examples
    test_str = "Hello, World!"
    print("\nOriginal string:", test_str)
    
    print("\nReversed string:")
    print(reverse_string(test_str))
    
    print("\nSplitting and joining string:")
    parts, joined = split_and_join("Python is fun", " ")
    print("Parts:", parts)
    print("Joined:", joined)
    
    print("\nChanging case:")
    print(change_case(test_str))
    
    print("\nReplacing substring:")
    print(replace_substring(test_str, "World", "Python"))
    
    print("\nStripping whitespace:")
    print(strip_whitespace("   Lots of space   "))
    
    print("\nFinding substring:")
    print(f"Position of 'World' in '{test_str}':", find_substring(test_str, "World"))
    
    print("\nRegex find (finding all 5-letter words):")
    regex_result = regex_find(r"\b\w{5}\b", "Hello there, these words: apple, world, and peace.")
    print(regex_result)
    
    print("\nIterating over lines in a multi-line string:")
    multiline = "Line one\nLine two\nLine three"
    iterate_lines(multiline)
    
    print("\nIterating over words in a sentence:")
    iterate_words("Iterate through each word in this sentence.")

