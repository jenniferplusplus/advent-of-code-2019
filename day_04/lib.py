def valid_sequence(val: int) -> bool:
    digits = list(str(val))
    i = 0
    for d in digits[:-1]:
        i += 1
        if int(d) > int(digits[i]):
            return False
    return True


def valid_pairs(val: int) -> bool:
    digits = list(str(val))
    i = 0
    for d in digits[:-1]:
        i += 1
        if d == digits[i]:
            return True
    return False


def valid_pairs_v2(val: int) -> bool:
    digits = list(str(val))
    i = 0
    while i < len(digits):
        count = duplicate_len(digits[i:])
        if count == 2:
            return True
        i += count
    return False


def duplicate_len(digits: []) -> int:
    position = 0
    length = 1
    prev = None

    for d in digits:
        if prev == None:
            prev = d
            continue
        if prev == d:
            length += 1
        else:
            break
    # while digits[position] == digits[position + 1]:
    #     position += 1
    #     length += 1
    #     if position + 1 >= len(digits):
    #         break

    return length
