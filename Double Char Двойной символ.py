# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# Examples (Input -> Output):

# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# Good Luck!

# Если задана строка, вы должны вернуть строку, в которой каждый символ (с учетом регистра) повторяется один раз.
# Примеры (ввод -> Вывод):

# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# Удачи!
def double_char(s):
    new_string = ""
    for char in s:
        new_string = new_string + char * 2
    return new_string


print(double_char("String"), "SSttrriinngg")
print(double_char("Hello World"), "HHeelllloo  WWoorrlldd")
print(double_char("1234!_ "), "11223344!!__  ")
