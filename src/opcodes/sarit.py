def add_hlrr(cpu, r_1, r_2):
    # TODO: finish
    # add HL,rr
    # -0hc
    value = (cpu.registers[r_1] << 8) + cpu.registers[r_2]
    pass


def inc_rr(cpu, r_1, r_2):
    # inc rr
    pass


def dec_rr(cpu, r_1, r_2):
    # dec rr
    pass


def add_spdd(cpu, dd):
    # add SP,dd
    pass


def ld_hlspdd(cpu, dd):
    # ld HL,SP+dd
    pass