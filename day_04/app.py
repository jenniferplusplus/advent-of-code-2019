from day_04.lib import valid_pairs, valid_sequence, valid_pairs_v2

input = [153517, 630395]
test_value = input[0]
result = []
result_v2 = []

while test_value < input[1]:
    if valid_sequence(test_value) and valid_pairs(test_value):
        result.append(test_value)
    if valid_sequence(test_value) and valid_pairs_v2(test_value):
        result_v2.append(test_value)
    test_value += 1

print(result)
print(f'found {len(result)} possible combinations')

print(result_v2)
print(f'found {len(result_v2)} possible combinations with the revised criteria')
