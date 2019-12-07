from day_04.lib import valid_pairs, valid_sequence

input = [153517, 630395]
test_value = input[0]
result = []

while test_value < input[1]:
    if valid_sequence(test_value) and valid_pairs(test_value):
        result.append(test_value)
    test_value += 1

print(result)
print(f'found {len(result)} possible combinations')
