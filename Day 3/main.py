# 🧩 Day 3 Problem: Remove Duplicates from a List
# 📜 Description

# Given a list of integers, return a new list that contains each number only once, keeping the original order of appearance.

# 💡 Example
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: [1, 2, 3, 4]

# Input: [5, 5, 5, 5]
# Output: [5]

# Input: [7, 8, 9]
# Output: [7, 8, 9]


def remove_duplicates(nums: list[int]) -> list[int]:
    map = {}
    for num in nums:
        if num not in map:
            map[num] = True
            
    return list(map.keys())


def main():
    array = [1, 2, 2, 3, 1, 4, 2]
    print(remove_duplicates(array))

if __name__ == "__main__":
    main()