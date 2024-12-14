# Timmy & Sarah think they are in love, but around where they live,
# they will only know once they pick a flower each. If one of the flowers
# has an even number of petals and the other has an odd number of petals
# it means they are in love.

# Write a function that will take the number of petals of each flower
# and return true if they are in love and false if they aren't.

# Тимми и Сара думают, что они влюблены, но в том месте, где они живут,
# они узнают об этом только после того, как сорвут по цветку.
# Если у одного из цветков четное количество лепестков,
# а у другого - нечетное количество лепестков , это означает, что они влюблены.

# Напишите функцию, которая будет вычислять количество лепестков каждого цветка
# и возвращать значение true, если они влюблены, и значение false, если это не так.


def lovefunc(flower1, flower2):

    return bool((flower1+flower2)%2)

# Тест
print(lovefunc(1, 4))
print(lovefunc(2, 2))
print(lovefunc(0, 1))
print(lovefunc(0, 0))


"""
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
"""

