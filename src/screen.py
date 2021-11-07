class Screen:
    def __init__(self, memory):
        self.memory = memory

    # TODO: this is temporary to test de boot screen, gotta implement
    # the i/o registers
    @property
    def scy(self):
        return self.memory.read_data(0xFF42)

    @property
    def scx(self):
        return self.memory.read_data(0xFF43)

    @property
    def ly(self):
        return self.memory.read_data(0xFF44)

    @property
    def lyc(self):
        return self.memory.read_data(0xFF45)

    @property
    def wy(self):
        return self.memory.read_data(0xFF4A)

    @property
    def wx(self):
        return self.memory.read_data(0xFF4B)
    # TODO: this is just a test!
    @property
    def screen(self):
        pointer = 0x8000
        tiles = []
        for y in range(32):
            for x in range(32):
                tile = []
                for _ in range(16):
                    tile.append(self.memory.read_data(pointer))
                    pointer += 1
        return tiles


