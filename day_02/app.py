import sys
from day_02.lib import IntCodeProcessor

input = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 1, 19, 9, 23, 1, 23, 9, 27, 1, 10, 27, 31, 1, 13,
         31, 35, 1, 35, 10, 39, 2, 39, 9, 43, 1, 43, 13, 47, 1, 5, 47, 51, 1, 6, 51, 55, 1, 13, 55, 59, 1, 59, 6, 63, 1,
         63, 10, 67, 2, 67, 6, 71, 1, 71, 5, 75, 2, 75, 10, 79, 1, 79, 6, 83, 1, 83, 5, 87, 1, 87, 6, 91, 1, 91, 13, 95,
         1, 95, 6, 99, 2, 99, 10, 103, 1, 103, 6, 107, 2, 6, 107, 111, 1, 13, 111, 115, 2, 115, 10, 119, 1, 119, 5, 123,
         2, 10, 123, 127, 2, 127, 9, 131, 1, 5, 131, 135, 2, 10, 135, 139, 2, 139, 9, 143, 1, 143, 2, 147, 1, 5, 147, 0,
         99, 2, 0, 14, 0]

# int_code = str.split(sys.argv[1], ',')
icp = IntCodeProcessor(input[:])
icp.process_int_code()

print(f'initial calculation: ({icp.int_code[0]})')

for noun in range(0, 99):
    for verb in range(0, 99):
        icp.reset()
        icp.int_code[1] = noun
        icp.int_code[2] = verb
        icp.process_int_code()
        if icp.int_code[0] == 19690720:
            print(f'found starting values ({noun:02d}{verb:02d})')
            print(icp.int_code[0])
            exit(0)

print('did not find any successful input values')
