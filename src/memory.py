class Memory:
    def __init__(self):
        self.ram = bytearray(8192)
        self.vram = bytearray(8192)
        self.cartridge = bytearray()

    def load_cartridge(self, path):
        rom_data = []
        with open(path, 'rb') as rom:
            for byte_ in rom.read():
                rom_data.append(byte_)
        self.cartridge = bytearray(rom_data)

