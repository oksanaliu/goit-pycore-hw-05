import re

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func):
    numbers_generator = func(text)
    total = sum(numbers_generator)
    return total

def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

text = read_text('text.txt')
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")