numbers = [str(i) for i in range(500, 3001) if i % 7 == 0 and i % 5 != 0]
number_string = ''.join(numbers)
count_21 = number_string.count('21')
number_string = number_string.replace('21', 'XX')

print(f"Numbers as a string: {number_string}")
print(f"Occurrences of '21': {count_21}")
