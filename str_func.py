def convert_to_uppercase(input_string):
    """
    Функция принимает строку изменяет регистр букв.
    """
    return input_string.upper()


def capitalize_first_letters(input_string):
    """
    Функция принимает строку и возвращает её с заглавными первыми буквами каждого слова.
    """
    return ' '.join(word.capitalize() for word in input_string.split())