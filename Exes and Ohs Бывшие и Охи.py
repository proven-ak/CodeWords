# Description:
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false
#
# Описание:
# Проверьте, содержит ли строка одинаковое количество символов "x" и "o". Метод должен возвращать логическое значение и не учитывать регистр символов. Строка может содержать любой символ.
#
# Примеры ввода/вывода:
#
# XO("ooxx") => истина
# XO("xooxx") => ложь
# XO("ooxXm") => истина
# XO("zpzpzpp") => true // при отсутствии "x" и "o" должно быть возвращено значение true
# XO("zzoo") => false

def xo(s):

    return s.lower().count('x') == s.lower().count('o')



print(xo("ooxx"), True)
print(xo("xooxx"), False)
print(xo("ooxXm"), True)
print(xo("zpzpzpp"), True)
print(xo("zzoo"), False)