def from_a1_to_rxcy(a1):
    row = ''
    col = ''
    for char in a1:
        if char.isdigit():
            row += char
        else:
            col += char
    col_num = 0
    for i, char in enumerate(col[::-1]):
        col_num += (ord(char) - ord('A') + 1) * (26 ** i)
    return f'R{row}C{col_num}'

def from_rxcy_to_a1(rxcy):
    row = ''
    col = ''
    for char in rxcy[1:]:
        if char == 'C':
            break
        row += char
    col_num = int(rxcy[len(row) + 2:])
    col_str = ''
    while col_num > 0:
        col_num, remainder = divmod(col_num , 26)
        if remainder == 0:
            col_num -= 1
            remainder = 26
        col_str = chr(64 + remainder) + col_str
    return col_str + row

n = int(input())
for _ in range(n):
    cell = input()
    if 'R' in cell and 'C' in cell:
        print(from_rxcy_to_a1(cell))
    else:
        print(from_a1_to_rxcy(cell))

#print(from_rxcy_to_a1('R26C26'))
#print(from_a1_to_rxcy('Z26'))