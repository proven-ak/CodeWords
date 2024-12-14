# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
#
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# Завершите выполнение функции, которая принимает строковый параметр
# и изменяет каждое слово в строке на противоположное.
# Все пробелы в строке должны быть сохранены.
#
# Примеры
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
new_list = []
new_str = ""


def reverse_words(text):
    new_list = []
    new_str = ""

    for char in text:
        if char != " ":
            new_str = char + new_str

        if char == " " and len(new_str) > 0:
            new_list.append(str(new_str))

        if char == " ":
            new_list.append(str(char))
            new_str = ""

        print("+++", new_str, char, new_list)

    print("***", "".join(new_list))
    return ("".join(new_list))


print('apple', "  ***  ", reverse_words('apple'), "  ***  ", 'elppa')
# print('The quick brown fox jumps over the lazy dog.', "  ***  ", reverse_words('The quick brown fox jumps over the lazy dog.'), "  ***  ", 'ehT kciuq nworb xof spmuj revo eht yzal .god')
# print('a b c d', "  ***  ", reverse_words('a b c d'), "  ***  ", 'a b c d')
# print('  double  spaced  words  ', "  ***  ", reverse_words('  double  spaced  words  '), "  ***  ", '  elbuod  decaps  sdrow  ')