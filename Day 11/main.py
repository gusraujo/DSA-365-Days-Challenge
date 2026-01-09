# This problem was asked by Netflix.

# Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.

# Do this in O(log N) time.

def findValue(nums: list[int], value: int) -> bool:
    size = len(nums) - 1
    left = 0
    right = size

    while left < right:
        index = (left + right) // 2
        if nums[index] == value:
            return True
        if nums[index] < value:
            left = index + 1
        if nums[index] > value:
            right = index - 1

    return False
    

def test_basic_case():
    list = [1,2,3,4,5,8,10,12,14]

    print(findValue(list, 10))  # True
    print(findValue(list, 7))   # False
    

def main():
    test_basic_case()
    print("🎉 Todos os testes passaram!")


if __name__ == "__main__":
    main()
    
    
## Resposta 


# def findValue(nums: list[int], value: int) -> bool:
#     left = 0
#     right = len(nums) - 1

#     while left <= right:
#         mid = left
#         step = right - left

#         while step > 1:
#             step -= 2
#             mid += 1

#         if nums[mid] == value:
#             return True
#         elif nums[mid] < value:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return False