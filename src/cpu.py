from opcodes.pointer import fetch_opc_info
from memory import Memory


class CPU:
    def __init__(self, memory):
        self.opcode = 0  # Stores current fetched opcode
        self.opcode_info = None

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
        self.memory = memory

    def setup(self) -> None:
        """
        Makes the initial set-up for the Cpu
        """
        self.registers['PC'] = 0x0000

    def cycle(self):
        # Read current memory address
        code = self.memory.read_data(self.registers['PC'])
        print(f'Fetched value: {hex(code)}')
        self.registers['PC'] += 1
        # Check if it's the code's header
        if not self.opcode_info:
            self.opcode_info = fetch_opc_info(self, code)
            return


    def __fetch_opcode(self):
        code = self.memory.read_data(self.registers['PC'])
        self.registers['PC'] += 1

        # TODO: this should only FETCH the code
        info = fetch_opc_info(self, code)
        args = []
        for _ in range(info.len):
            arg = self.memory.read_data(self.registers['PC'])
            args.append(arg)
            self.registers['PC'] += 1
        all_args = info.args + args
        info.func(*all_args)


