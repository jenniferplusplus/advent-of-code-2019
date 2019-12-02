import sys
from day_01.lib import fuel_calc


weights = sys.argv[1::]
fuel = 0

for weight in weights:
    fuel += fuel_calc(int(weight))

print(f'calculated fuel requirement for {len(weights)} modules')
print(fuel)
