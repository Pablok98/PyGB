class Cartridge:
    def __init__(self):
        self.cartridge = bytearray()

    def load_cartridge(self, path):
        # TODO: MBC and real load
        rom_data = []
        with open(path, 'rb') as rom:
            for byte_ in rom.read():
                rom_data.append(byte_)
        self.cartridge = bytearray(rom_data)