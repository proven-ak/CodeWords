"""
Дан треугольник из последовательных нечетных чисел:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Вычислите сумму чисел в n-й строке этого треугольника (начиная с индекса 1), например: (Ввод -> Вывод)

1 -->  1
2 --> 3 + 5 = 8
"""

def row_sum_odd_numbers(n):
    num = -1
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            num += 2
            if i == n:
                sum += num
    return sum


"""
def row_sum_odd_numbers(n):
    return sum(range(n*(n-1)+1, n*(n+1), 2))
"""




print(row_sum_odd_numbers(1), "1")
print(row_sum_odd_numbers(2), "8")
print(row_sum_odd_numbers(13), "2197")
print(row_sum_odd_numbers(19), "6859")
print(row_sum_odd_numbers(41), "68921")