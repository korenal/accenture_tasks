"""This is program which counts backwards from 100 to 1 and  prints: “Agile” if the number is divisible by 5, \
 “Software” if the number is divisible by 3, “Testing” if the number is divisible by both, or prints just the number \
 if none of those cases are true"""

print(*map(
    lambda x: "Testing" * ((x % 3 == 0) and (x % 5 == 0)) + 'Agile' * ((x % 5 == 0) and (x % 3 != 0)) + 'Software' * (
                (x % 3 == 0) and (x % 5 != 0)) or x, range(100, 0, -1)), sep='\n')
