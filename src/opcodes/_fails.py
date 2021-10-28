# BINARY STUFF
def load_rRR(cpu, t, f_1, f_2):
    # LD r,(HL)
    """
    first = bin(cpu.registers[f_1])[2:].zfill(4)
    second = bin(cpu.registers[f_2])[2:].zfill(4)
    """
    first = (cpu.registers[f_1] << 8) & 0xFF00
    second = cpu.registers[f_2]
    cpu.registers[t] = hex(first + second)


def load_RRr(cpu, t_1, t_2, f):
    # LD (HL),R
    binary = bin(cpu.registers[f])[2:0].zfill(8)
    cpu.registers[t_1] = hex(int(binary[:4], 2))
    cpu.registers[t_2] = hex(int(binary[4:], 2))


def load_RRn(cpu, t_1, t_2, n):
    # LD (HL),n
    binary = bin(n)[2:0].zfill(8)
    cpu.registers[t_1] = hex(int(binary[:4], 2))
    cpu.registers[t_2] = hex(int(binary[4:], 2))