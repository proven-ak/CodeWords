# Even or Odd
# Create a function that takes an integer as an argument and
# returns "Even" for even numbers or "Odd" for odd numbers.


# Четный или Нечетный
# Создайте функцию, которая принимает целое число в качестве аргумента
# и возвращает "Even" для чётных чисел или "Odd" для нечётных чисел.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

    # return "Even" if number % 2 else return "Odd"


print(even_or_odd(1), "Odd")
print(even_or_odd(2), "Even")
print(even_or_odd(-1), "Odd")
print(even_or_odd(-2), "Even")
print(even_or_odd(0), "Even")