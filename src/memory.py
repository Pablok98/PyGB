from .cartridge import Cartridge
from .config import ROM_PATH


class Memory:
    def __init__(self):
        self.wram = bytearray(8192)
        self.vram = bytearray(8192)
        self.cartridge = Cartridge()
        self.io_registers = bytearray(128)

    def load_cartridge(self, path):
        # TODO: fix
        self.cartridge.load_cartridge(path)

    def read_data(self, address):
        # TODO: once upgrded to python 3.10, compress both match cases
        # into one
        if 0x0000 <= address <= 0x3FFF:
            return self.cartridge.read_data(address)
        elif 0x4000 <= address <= 0x7FFF:
            return self.cartridge.read_data(address)
        elif 0x8000 <= address <= 0x9FFF:
            return self.vram[address - 0x8000]
        elif 0xA000 <= address <= 0xBFFF:
            return self.cartridge.read_ram(address - 0xA000)
        elif 0xC000 <= address <= 0xCFFF:
            return self.wram[address - 0xC000]
        elif 0xD000 <= address <= 0xDFFF:
            return self.wram[address - 0xC000]
        elif 0xE000 <= address <= 0xFDFF:
            pass
        elif 0xFE00 <= address <= 0xFE9F:
            pass
        elif 0xFEA0 <= address <= 0xFEFF:
            pass
        elif 0xFF00 <= address <= 0xFF7F:
            return self.io_registers[address - 0xFF00]
        elif 0xFF80 <= address <= 0xFFFE:
            pass
        elif 0xFFFF <= address <= 0xFFFF:
            pass

    def write_data(self, data, address):
        if 0x0000 <= address <= 0x3FFF:
            self.cartridge.write_data(data, address)
        elif 0x4000 <= address <= 0x7FFF:
            self.cartridge.write_data(data, address)
        elif 0x8000 <= address <= 0x9FFF:
            self.vram[address - 0x8000] = data
        elif 0xA000 <= address <= 0xBFFF:
            self.cartridge.write_ram(data, address - 0xA000)
        elif 0xC000 <= address <= 0xCFFF:
            self.wram[address - 0xC000] = data
        elif 0xD000 <= address <= 0xDFFF:
            self.wram[address - 0xC000] = data
        elif 0xE000 <= address <= 0xFDFF:
            pass
        elif 0xFE00 <= address <= 0xFE9F:
            pass
        elif 0xFEA0 <= address <= 0xFEFF:
            pass
        elif 0xFF00 <= address <= 0xFF7F:
            self.io_registers[address - 0xFF00] = data
        elif 0xFF80 <= address <= 0xFFFE:
            pass
        elif 0xFFFF <= address <= 0xFFFF:
            pass
