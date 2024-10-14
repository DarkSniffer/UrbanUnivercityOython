first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# First result
first_result = []
for s in first_strings:
    if len(s) >= 5:
        first_result.append(len(s))

# Second result
second_result = []
for s1 in first_strings:
    for s2 in second_strings:
        if len(s1) == len(s2):
            second_result.append((s1, s2))

# Third result
third_result = {}
for s in first_strings + second_strings:
    if len(s) % 2 == 0:
        third_result[s] = len(s)

# Print the results
print(first_result)
print(second_result)
print(third_result)