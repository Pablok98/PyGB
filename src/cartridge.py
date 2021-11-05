from os.path import join

rom_size = {
    0x00: 2,
    0x01: 4,
    0x02: 8,
    0x03: 16,
    0x04: 32,
    0x05: 64,
    0x06: 128,
    0x07: 256,
    0x08: 512,
    0x52: 72,  # Unofficial
    0x53: 80,  # Unofficial
    0x54: 96   # Unofficial
}
ram_size = {
    0x00: 0,
    0x01: 0,
    0x02: 1,
    0x03: 4,
    0x04: 16,
    0x05: 8
}


class Cartridge:
    def __init__(self):
        self.cart_data = bytearray()
        self.rom_banks = []
        self.ram_banks = []
        self.current_bank = 0x01
        self.ram_pointer = 0x00

    def load_cartridge(self, path):
        rom_data = []
        with open(path, 'rb') as rom:
            for byte_ in rom.read():
                rom_data.append(byte_)
        self.cart_data = bytearray(rom_data)
        self.burn_boot()
        self.setup_mbc()

    def burn_boot(self):
        # TODO: unhardcode and research legal stuff xd
        with open(join('..', 'roms', 'boot.gb'), 'rb') as rom:
            for i, byte_ in enumerate(rom.read()):
                self.cart_data[i] = byte_

    def setup_mbc(self):
        pass

    def write_data(self, data, address):
        pass

    def read_data(self, address):
        return self.cart_data[address]


class CartridgeMBC1(Cartridge):
    def __init__(self):
        super().__init__()
        self.bank_mode = 0

    def setup_mbc(self):
        n_banks = rom_size[self.cart_data[0x148]]
        for i in range(n_banks):
            self.rom_banks.append(self.cart_data[0x4000 * i:0x4000 * (i + 1)])
        n_banks = ram_size[self.cart_data[0x149]]
        for _ in range(n_banks):
            self.ram_banks.append(bytearray(0x1FFF))

    def read_data(self, address):
        if 0x0000 <= address <= 0x3FFF:
            return self.cart_data[address]
        elif 0x4000 <= address <= 0x7FFF:
            address = address - (self.current_bank * 0x4000)
            return self.rom_banks[self.current_bank][address]
        elif 0xA000 <= address <= 0xBFFF:
            address = address - (self.ram_pointer * 0x1FFF)
            return self.cart_data[address]
        # Every other address can't be read

    def write_data(self, data, address):
        if 0x0000 <= address <= 0x1FFF:
            # todo: ram enable
            pass
        elif 0x2000 <= address <= 0x3FFF:
            self.set_rombank(data)
        elif 0x4000 <= address <= 0x5FFF:
            self.set_rambank(data)
        elif 0x6000 <= address <= 0x7FFF:
            self.set_rrmode(data)
        elif 0xA000 <= address <= 0xBFFF:
            address = address - (self.current_bank * 0x4000)
            self.rom_banks[self.current_bank][address] = data

    def set_rrmode(self, data):
        self.bank_mode = data

    def set_rombank(self, data):
        bank = int(bin(data)[5:].zfill(8), 2)
        self.current_bank = bank
        if self.current_bank in [0x00, 0x20, 0x40, 0x60]:
            self.current_bank += 1

    def set_rambank(self, data):
        if self.bank_mode == 0:
            self.current_bank += data << 5
            if self.current_bank in [0x00, 0x20, 0x40, 0x60]:
                self.current_bank += 1


