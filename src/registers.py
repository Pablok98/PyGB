class Registers:
    def __init__(self):
        # 8-bit registers
        self.A = 0  # High accumulator and flags
        self.F = 0  # Low   ´´
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.H = 0
        self.L = 0
        # 16-bit registers
        self.SP = 0
        self.PC = 0
