first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# First result
first_result = []
for s1, s2 in zip(first, second):
    if len(s1) != len(s2):
        first_result.append(len(s1) - len(s2))

# Second result
second_result = []
for i in range(len(first)):
    second_result.append(len(first[i]) == len(second[i]))

# Print the results
print(first_result)
print(second_result)