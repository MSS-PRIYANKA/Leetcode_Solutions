def xorOperation(self, n: int, start: int) -> int:
    res = []
    for i in range(0, n):
        res.append(start+2 * i)
    print(res)
    return reduce(ixor, res)
