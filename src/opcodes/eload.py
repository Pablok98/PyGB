def load_rr(cpu, f, t):
    # LD r,r'
    cpu.registers[t] = cpu.registers[f]


def load_rn(cpu, r, n):
    # LD r,n
    cpu.registers[r] = n


def load_rhl(cpu, r, f_1, f_2):
    # LD r,(HL)
    first = (cpu.registers[f_1] << 8) & 0xFF00
    second = cpu.registers[f_2]
    cpu.registers[r] = cpu.memory.read_data(first + second)


def load_hlr(cpu, t_1, t_2, r):
    # LD (HL),r
    first = (cpu.registers[t_1] << 8) & 0xFF00
    second = cpu.registers[t_2]
    target = first + second
    # Data, address
    cpu.memory.write_data(cpu.registers[r], target)


def load_RRn(cpu, t_1, t_2, n):
    # LD (HL),n
    first = (cpu.registers[t_1] << 8) & 0xFF00
    second = cpu.registers[t_2]
    target = first + second
    cpu.memory.write_data(n, target)


def ld_Rnn(cpu, t, nn):
    # LD A,(nn)
    cpu.registers[t] = cpu.memory.read_data(nn)


def nnR(cpu, nn, r):
    # LD (nn),A
    cpu.memory.write_data(cpu.registers[r], nn)


def ldhAC(cpu):
    # LDH A,(C)
    address = 0xFF00 + cpu.registers['C']
    cpu.registers['A'] = cpu.memory.read_data(address)


def ldhCA(cpu):
    # LDH (C),A
    address = 0xFF00 + cpu.registers['C']
    cpu.memory.write_data(cpu.registers['A'], address)


def ldhAn(cpu, n):
    # LDH A,(n)
    address = 0xFF00 + n
    cpu.registers['A'] = cpu.memory.read_data(address)


def ldhnA(cpu, n):
    # LDH (n),A
    address = 0xFF00 + n
    cpu.memory.write_data(cpu.registers['A'], address)


def lddahl(cpu):
    # LD A, (Hl-)
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = first + second
    cpu.registers['A'] = cpu.memory.read_data(value)

    # DECREMENT HL VALUE
    new_value = value - 1
    cpu.registers['H'] = (new_value & 0xFF00) >> 8
    cpu.registers['L'] = new_value & 0x00FF


def lddgla(cpu):
    # LD (Hl-),A
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = first + second
    cpu.memory.write_data(cpu.registers['A'], value)
    new_value = value - 1
    cpu.registers['H'] = (new_value & 0xFF00) >> 8
    cpu.registers['L'] = new_value & 0x00FF


def ldiahl(cpu):
    # LD A, (Hl+)
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = first + second
    cpu.registers['A'] = cpu.memory.read_data(value)

    # Increment HL VALUE
    new_value = value + 1
    cpu.registers['H'] = (new_value & 0xFF00) >> 8
    cpu.registers['L'] = new_value & 0x00FF


def ldigla(cpu):
    # LD (Hl+),A
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = first + second
    cpu.memory.write_data(cpu.registers['A'], value)
    new_value = value + 1
    cpu.registers['H'] = (new_value & 0xFF00) >> 8
    cpu.registers['L'] = new_value & 0x00FF


