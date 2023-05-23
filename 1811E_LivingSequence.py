def convert_to_base(number, base):
    if number == 0:
        return '0'
    digits = []
    while number:
        number, digit = divmod(number, base)
        digits.append(str(digit if digit < 4 else digit + 1))
    return ''.join(digits[::-1])

for _ in range(int(input())):
    num = int(input())
    convert = convert_to_base(num, 9)
    print(convert)