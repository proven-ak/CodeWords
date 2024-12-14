# Write a function that takes an array of numbers and returns
# the sum of the numbers. The numbers can be negative or non-integer.
# If the array does not contain any numbers then you should return 0.

# Напишите функцию, которая принимает массив чисел и возвращает
# сумму чисел. Числа могут быть отрицательными или нецелочисленными.
# Если массив не содержит чисел, то вы должны вернуть 0.


def sum_array(a):

    return sum(a)



print(sum_array([1, 5.2, 4, 0, -1]))
print(sum_array([]))
print(sum_array([-2.398]))
print(sum_array(range(101)))





"""
import codewars_test as test
from solution import sum_array

@test.describe("Testing sum array")
def tests():
    @test.it("Fixed tests")
    def fixed_tests(): 
        test.assert_equals(sum_array([]), 0)
        test.assert_equals(sum_array([1, 2, 3]), 6)
        test.assert_equals(sum_array([1.1, 2.2, 3.3]), 6.6)
        test.assert_equals(sum_array([4, 5, 6]), 15)
        test.assert_equals(sum_array(range(101)), 5050)
"""
