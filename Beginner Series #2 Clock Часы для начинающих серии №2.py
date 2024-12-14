# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since
# midnight in milliseconds.

# Часы показывают h часов, m минут и s секунд после полуночи.

# Ваша задача - написать функцию, которая возвращает время, прошедшее с
# полуночи в миллисекундах.

def past(h, m, s):
    return (((h * 60 + m) * 60) + s) * 1000


print(past(0, 1, 1), 61000)
print(past(1, 1, 1), 3661000)
print(past(0, 0, 0), 0)
print(past(1, 0, 1), 3601000)
print(past(1, 0, 0), 3600000)