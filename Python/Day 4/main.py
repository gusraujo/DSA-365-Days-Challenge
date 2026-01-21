# 🧩 Day 4 Problem: Check if a String is a Palindrome
# 📜 Description

# Write a function that checks if a string reads the same forward and backward — ignoring spaces, punctuation, and case differences.

# 💡 Examples
# Input: "Racecar"
# Output: True

# Input: "A man a plan a canal Panama"
# Output: True

# Input: "Python"
# Output: False

# ⚙️ Requirements

# Create a function:

# def is_palindrome(s: str) -> bool:


# The comparison should ignore:

# Upper/lowercase differences

# Spaces and non-letter characters

# Return True if it’s a palindrome, else False.

def is_palindrome(s: str) -> bool:
    s = s.lower()
    length = len(s)
    for i in range(length//2) :
        if s[i] != s[length - 1 - i]:
            return False
    return True
        

def main():
    print(is_palindrome("racecar"))   # True
    print(is_palindrome("madam"))     # True
    print(is_palindrome("python"))    # False

if __name__ == "__main__":
    main()