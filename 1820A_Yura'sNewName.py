t = int(input().strip())
for _ in range(t):
    s = input().strip()
    ops = 0
    caret_count = 0
    underscore_count = 0
    for ch in s:
        if ch == '^':
            if underscore_count > 0:
                ops += max(0, 2 - caret_count)
                caret_count = 1
                underscore_count = 0
            else:
                caret_count += 1
        else: # ch == '_'
            underscore_count += 1
    if underscore_count > 0:
        ops += max(0, 2 - caret_count)
    print(ops)