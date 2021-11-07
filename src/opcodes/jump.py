from utils import hex_to_lbin, lbin_to_hex


def jump_nn(cpu, n_1, n_2):
    # jp nn
    # [1] Jump to nn, PC=nn
    nn = (n_2 << 8) + n_1
    cpu.registers['PC'] = nn


def jump_hl(cpu):
    # jp HL
    # [1] jump to HL, PC=HL
    address = (cpu.registers['H'] << 8) + cpu.registers['L']
    cpu.registers['PC'] = address


def jump_fnn(cpu, cond, n_1, n_2):
    # jp f,nn
    # [1] conditional jump if nz,z,nc,c
    flag = hex_to_lbin(cpu.registers['F'])
    conditions = {
        'NZ': not bool(flag[7]),
        'NC': not bool(flag[4]),
        'Z': bool(flag[7]),
        'C': bool(flag[4]),

    }
    address = (n_2 << 8) + n_1
    if conditions[cond]:
        cpu.registers['PC'] = address


def jumpr_pcdd(cpu, d):
    # jr PC+dd
    # [1] relative jump to nn (PC=PC+8-bit signed)
    cpu.registers['PC'] += d


def jr_fpcdd(cpu, cond, d):
    # jr f,PC+dd
    # [1] conditional relative jump if nz,z,nc,c
    jump_fnn(cpu, cond, d, cpu.registers['PC'])


def call_nn(cpu, n_1, n_2):
    # call nn
    # [1] call to nn, SP=SP-2, (SP)=PC, PC=nn
    nn = (n_2 << 8) & n_1
    cpu.sp -= 2


    cpu.registers['S'] = cpu.registers['PC'] & 0xFF00
    cpu.sp += 1
    cpu.registers['P'] = cpu.registers['PC'] & 0x00FF
    cpu.registers['PC'] = nn


def call_fnn(cpu, cond, n_1, n_2):
    # call f,nn
    flag = hex_to_lbin(cpu.registers['F'])
    conditions = {
        'NZ': not bool(flag[7]),
        'NC': not bool(flag[4]),
        'Z': bool(flag[7]),
        'C': bool(flag[4]),

    }
    if conditions[cond]:
        call_nn(cpu, n_1, n_2)


def ret(cpu):
    # ret
    pass
    cpu.registers['SP']


def retf(cpu, cond):
    # ret f
    pass


def reti(cpu):
    # reti
    pass


def rst_n(cpu, n):
    # rst n
    pass


# [1] https://gbdev.io/pandocs/CPU_Instruction_Set.html
