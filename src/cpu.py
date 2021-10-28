from opcodes import execute_opc


class CPU:
    def __init__(self):
        self.opcode = 0  # Stores current fetched opcode

        # Register setup
        self.registers = {
            'A': 0,
            'F': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'H': 0,
            'L': 0,
            'SP': 0,
            'PC': 0
        }
        self.memory = None # TODO: memory controller

    def setup(self) -> None:
        """
        Makes the initial set-up for the Cpu
        """

        self.registers['PC'] = 0x0100

    def cycle(self):
        execute_opc(self)

