from .cartridge import Cartridge
from .config import ROM_PATH


class Memory:
    def __init__(self):
        self.ram = bytearray(8192)
        self.vram = bytearray(8192)
        self.cartridge = Cartridge()

    def load_cartridge(self, path):
        # TODO: fix
        self.cartridge.load_cartridge(path)

    def read_data(self, address):
        if 0x0000 <= address <= 0x3FFF:
            pass
        elif 0x4000 <= address <= 0x7FFF:
            pass
        elif 0x8000 <= address <= 0x9FFF:
            pass
        elif 0xA000 <= address <= 0xBFFF:
            pass
        elif 0xC000 <= address <= 0xCFFF:
            pass
        elif 0xD000 <= address <= 0xDFFF:
            pass
        elif 0xE000 <= address <= 0xFDFF:
            pass
        elif 0xFE00 <= address <= 0xFE9F:
            pass
        elif 0xFEA0 <= address <= 0xFEFF:
            pass
        elif 0xFF00 <= address <= 0xFF7F:
            pass
        elif 0xFF80 <= address <= 0xFFFE:
            pass
        elif 0xFFFF <= address <= 0xFFFF:
            pass

    def write_data(self, data, address):
        pass
