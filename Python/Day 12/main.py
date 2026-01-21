# Given a list of integers, return the largest product that can be made by multiplying any three integers.

# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.


def executeLargestProductOfThree(nums: list[int]) -> int:
    nums.sort()
    
    # The largest product can be either:
    # 1. The product of the three largest numbers
    # 2. The product of the two smallest numbers (which could be negative) and the largest number
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


def test_basic_case():
    lista = [1,8,6,2,5,4,8,3,7]
    
    resultado = executeLargestProductOfThree(lista)
    
    print(resultado)


def main():
    test_basic_case()
    print("🎉 Todos os testes passaram!")


if __name__ == "__main__":
    main()