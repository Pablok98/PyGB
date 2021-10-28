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


if __name__ == "__main__":
    gb = Gameboy()
    gb.load_rom()
    print((gb.memory.cartridge))