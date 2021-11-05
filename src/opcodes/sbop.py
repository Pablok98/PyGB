from utils import hex_to_lbin, lbin_to_hex


def bit_nr(cpu, n, r):
    # bit n,r
    # z01-
    flag = hex_to_lbin(cpu.registers['F'])[4]
    flag = [0, 0, 0, 0, flag, 1, 0, 0]
    bit = hex_to_lbin(cpu.registers[r])[n]
    flag[7] = bit


def bit_nhl(cpu, n):
    # bit n,(HL)
    pass


def set_nr(cpu, n, r):
    # set n,r
    pass


def set_nhl(cpu, n):
    # set n,(HL)
    pass


def res_nr(cpu, n, r):
    # res n,r
    pass


def res_nhl(cpu, n):
    # res n,(HL)
    pass