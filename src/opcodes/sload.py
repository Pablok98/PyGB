def load_rrnn(cpu, r_1, r_2, n_1, n_2):

    # LD rr,nn
    cpu.registers[r_1] = n_2
    cpu.registers[r_2] = n_1


def load_nnsp(cpu, nn):
    # LD (nn), SP
    cpu.registers['SP'] = nn


def load_sphl(cpu):
    # LD SP,HL
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    cpu.registers['SP'] = first + second


def push_rr(cpu, r_1, r_2):
    # PUSH rr
    # TODO: check stack pointer movement
    cpu.registers["SP"] -= 2
    cpu.memory.write_data(cpu.registers[r_1], cpu.registers["SP"])
    cpu.registers["SP"] += 1
    cpu.memory.write_data(cpu.registers[r_2], cpu.registers["SP"])


def pop_rr(cpu, r_1, r_2):
    # POP rr
    # TODO: Flag change on the F register
    cpu.registers[r_1] = cpu.memory.read_data(cpu.registers["SP"])
    cpu.registers["SP"] += 1
    cpu.registers[r_2] = cpu.memory.read_data(cpu.registers["SP"])
    cpu.registers["SP"] += 1