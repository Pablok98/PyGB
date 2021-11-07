from utils import hex_to_lbin, lbin_to_hex


def ccf(cpu):
    # ccf
    # -00c
    # TODO: optimize this ugly thing (flag extraction should be standard)
    flag, z = hex_to_lbin(cpu.registers['F'])[4], \
              hex_to_lbin(cpu.registers['F'])[7]
    flag = 0 if flag else 1
    flag = [0, 0, 0, 0, flag, 0, 0, z]
    cpu.registers['F'] = lbin_to_hex(flag)


def scf(cpu):
    # scf
    # -001
    z = hex_to_lbin(cpu.registers['F'])[7]
    flag = [0, 0, 0, 0, 1, 0, 0, z]
    cpu.registers['F'] = lbin_to_hex(flag)


def nop(cpu):
    # nop
    pass


def halt(cpu):
    # HALT
    pass


def stop(cpu):
    # stop
    pass


def di(cpu):
    # di
    pass


def ei(cpu):
    # ei
    pass
