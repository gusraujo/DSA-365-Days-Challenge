# Day 2 Problem: First Non-Repeating Character
# 📜 Description

# Given a string, find the first character that appears only once in it.
# If no such character exists, return None.

# ⚙️ Requirements

# Create a function:

# def first_unique_char(s: str) -> str | None:


# The function should return:

# The first non-repeated character (as a string), or

# None if every character repeats.

# Ignore case sensitivity (treat 'A' and 'a' as the same).

# You cannot use collections.Counter — implement manually.


def first_unique_char(s: str):
    s = s.lower()
    for char in s:
        if containsDuplicate(char, s) == False:
            return char
    return None

def containsDuplicate(c, s : str):
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count > 1

def main():
    test1 = "awssawye"
    print(first_unique_char(test1))

if __name__ == "__main__":
    main()


# Better solution 

# def first_unique_char(s: str):
#     s = s.lower()
#     counts = {}
#     for char in s:
#         counts[char] = counts.get(char, 0) + 1
#     for char in s:
#         if counts[char] == 1:
#             return char
#     return None