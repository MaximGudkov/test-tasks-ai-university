mustBeStringError = TypeError("Тип входящего объекта должен быть строкой")


def reverse_string(input_string: str):
    if not isinstance(input_string, str):
        raise mustBeStringError
    return input_string[::-1]


def is_palindrome(input_string):
    if not isinstance(input_string, str):
        raise mustBeStringError
    return input_string == input_string[::-1]


# Пример использования

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(reversed_string)

test_string = "anna"
result = is_palindrome(test_string)
print(result)
