from opcodes.pointer import fetch_opc_info
from memory import Memory


class CPU:
    def __init__(self, memory):
        # self.opcode = 0
        # self.opcode_info = None

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
            'S': 0,
            'P': 0,
            'PC': 0
        }
        self.memory = memory

    @property
    def sp(self):
        val = (self.registers['S'] << 8) + self.registers['P']
        return val

    @sp.setter
    def sp(self, value):
        self.registers['S'] = value & 0xFF00
        self.registers['P'] = value & 0x00FF

    def setup(self) -> None:
        """
        Makes the initial set-up for the Cpu
        """
        self.registers['PC'] = 0x0000

    def cycle(self):
        # Read current memory address
        # TODO: reorganize cb plus optional args
        code = self.memory.read_data(self.registers['PC'])
        print("===========================================")

        print(f'Fetched opcode: {hex(code)}')

        self.registers['PC'] += 1

        if code == 0xcb:
            code = self.memory.read_data(self.registers['PC'])

            print(f'Fetched 0xCB Opcode: {hex(code)}')

            self.registers['PC'] += 1
            info = fetch_opc_info(self, code, True)
            print(f'Opcode info: {info}')
            all_args = [self] + info.args
            info.func(*all_args)
            return

        info = fetch_opc_info(self, code)
        print(f'Opcode info: {info}')
        op_args = []
        for _ in range(info.len - 1):
            code = self.memory.read_data(self.registers['PC'])

            print(f'Fetched argument: {hex(code)}')

            op_args.append(code)
            self.registers['PC'] += 1
        all_args = [self] + info.args + op_args
        info.func(*all_args)



