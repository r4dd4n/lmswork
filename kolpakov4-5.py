import itertools

def check_equation(mapping, equation):
    # Заменяем буквы на цифры согласно маппингу
    for letter, digit in mapping.items():
        equation = equation.replace(letter, str(digit))
    # Проверяем, является ли уравнение верным
    left, right = equation.split('=')
    return eval(left) == eval(right)

def find_mapping(equation):
    # Извлекаем уникальные буквы из уравнения
    letters = set(filter(str.isalpha, equation))
    if len(letters) > 10:
        return "Слишком много уникальных букв для 10 цифр."
    
    # Генерируем все возможные комбинации цифр для уникальных букв
    for digits in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, digits))
        if check_equation(mapping, equation):
            return mapping
    return "Нет подходящего маппинга."

# Пример использования
equation = "A + B = C"
result = find_mapping(equation)
print(result)