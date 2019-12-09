def operation(code: int):
    switch = {
        1: op_add,
        2: op_mult,
        99: op_end
    }

    op = switch.get(int(code), None)
    if op is None:
        raise LookupError(f'{code} is not a valid op code')
    return op


class IntCodeProcessor:
    def __init__(self, int_code: []):
        self.int_code = int_code
        self.original_int_code = int_code[:]
        self.position = 0

    def next_code_block(self) -> []:
        result = self.int_code[self.position:self.position + 4]
        self.position += 4

        return result

    def process_code_block(self, code_block: []):
        # print(f'processing {code_block} at pos ({self.position - 4})')
        op = operation(code_block[0])
        p = code_block[1:]

        if len(p) < 3:
            return None

        result = op(self.int_code[p[0]], self.int_code[p[1]])

        if result is None:
            return result

        self.int_code[p[2]] = result
        return result

    def process_int_code(self):
        code_block = self.next_code_block()
        res = 0
        if len(code_block) != 4:
            return None

        while len(code_block) > 0 and res is not None:
            res = self.process_code_block(code_block)
            code_block = self.next_code_block()
        return self.int_code

    def reset(self):
        self.int_code = self.original_int_code[:]
        self.position = 0
        return


def op_add(left: int, right: int):
    return left + right


def op_mult(left: int, right: int):
    return left * right


def op_end(left, right):
    return None
