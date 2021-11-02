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


def load_Rnn(cpu, t, nn):
    # LD A,(nn)
    cpu.registers[t] = cpu.memory.read_data(nn)


def load_nnR(cpu, nn, r):
    # LD (nn),A
    cpu.memory.write_data(cpu.registers[r], nn)


def load_hAC(cpu):
    # LDH A,(C)
    address = 0xFF00 + cpu.registers['C']
    cpu.registers['A'] = cpu.memory.read_data(address)


def load_dhCA(cpu):
    # LDH (C),A
    address = 0xFF00 + cpu.registers['C']
    cpu.memory.write_data(cpu.registers['A'], address)


def load_hAn(cpu, n):
    # LDH A,(n)
    address = 0xFF00 + n
    cpu.registers['A'] = cpu.memory.read_data(address)


def load_hnA(cpu, n):
    # LDH (n),A
    address = 0xFF00 + n
    cpu.memory.write_data(cpu.registers['A'], address)


def load_dahl(cpu):
    # LD A, (Hl-)
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = first + second
    cpu.registers['A'] = cpu.memory.read_data(value)

    # DECREMENT HL VALUE
    new_value = value - 1
    cpu.registers['H'] = (new_value & 0xFF00) >> 8
    cpu.registers['L'] = new_value & 0x00FF


def load_dgla(cpu):
    # LD (Hl-),A
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = first + second
    cpu.memory.write_data(cpu.registers['A'], value)
    new_value = value - 1
    cpu.registers['H'] = (new_value & 0xFF00) >> 8
    cpu.registers['L'] = new_value & 0x00FF


def load_iahl(cpu):
    # LD A, (Hl+)
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = first + second
    cpu.registers['A'] = cpu.memory.read_data(value)

    # Increment HL VALUE
    new_value = value + 1
    cpu.registers['H'] = (new_value & 0xFF00) >> 8
    cpu.registers['L'] = new_value & 0x00FF


def load_igla(cpu):
    # LD (Hl+),A
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = first + second
    cpu.memory.write_data(cpu.registers['A'], value)
    new_value = value + 1
    cpu.registers['H'] = (new_value & 0xFF00) >> 8
    cpu.registers['L'] = new_value & 0x00FF


def ld_iofrom(cpu, n):
    # ld A,(FF00+n)
    pass


def ld_ioto(cpu, n):
    # ld (FF00+n),A
    pass


def ld_iofromc(cpu):
    # LD A,(FF00+C)
    pass


def ld_iotoc(cpu):
    # LD (FF00+C),A
    pass