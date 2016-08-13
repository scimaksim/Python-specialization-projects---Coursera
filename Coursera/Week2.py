import re
fhand = open('regex_sum_301436.txt')

final_value = 0

for line in fhand:
    number = re.findall('([0-9]+)', line)
    if number:
        for i in number:
            final_value += int(i)
    else:
        continue

print final_value

