from cpu import CPU
from memory import Memory
from screen import Screen
import config as c


class Gameboy:
    def __init__(self):
        self.cpu = CPU()

        # Memory setup
        self.memory = Memory()

        # Screen setup
        self.screen = Screen()

    def load_rom(self, path=c.ROM_PATH):
        self.memory.load_cartridge(path)

    def test_command(self):
        self.cpu.fetch_opcode()



if __name__ == "__main__":
    rom_data = []
    with open(c.ROM_PATH, 'rb') as rom:
        for byte_ in rom.read():
            rom_data.append(byte_)
    cartridge = bytearray(rom_data)
    print(len(cartridge))
    gb = Gameboy()
    gb.load_rom()
    print((gb.memory.cartridge))