class Byte:
    def __init__(self, value=0):
        self.value = bytearray(1)
        self.value[0] = value

    def __add__(self, other):
        return self.value[0] + other

    def __repr__(self):
        return str(hex(self.value[0]))


if __name__ == "__main__":
    bait = Byte(10)
    bait += 1
    print(bait)
