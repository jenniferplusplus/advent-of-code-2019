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

