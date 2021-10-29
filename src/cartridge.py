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

    def write_data(self, data, address):
        pass

    def read_data(self, address):
        pass

    def read_ram(self, address):
        pass

    def write_ram(self, data, address):
        pass