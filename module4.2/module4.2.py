from fake_math import fake_divide as fake_div
from true_math import true_divide as true_div

# Testing the functions



result1 = fake_div(69, 3)
result2 = fake_div(3, 0)
result3 = true_div(49, 7)
result4 = true_div(15, 0)

print(f"Результат ложного деления: {result1}")
print(f"Результат ложного деления: {result2}")
print(f"Результат истинного деления: {result3}")
print(f"Результат истинного деления: {result4}")