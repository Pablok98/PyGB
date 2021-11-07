from utils import hex_to_lbin, lbin_to_hex


def add_hlrr(cpu, r_1, r_2):
    # add HL,rr
    # -0hc
    # [1] HL = HL+rr ; rr may be BC,DE,HL,SP

    value = (cpu.registers[r_1] << 8) + cpu.registers[r_2]
    hl_val = (cpu.registers['H'] << 8) + cpu.registers['L']
    new_val = value + hl_val
    cpu.registers['H'] = new_val & 0xFF00
    cpu.registers['L'] = new_val & 0x00FF


def inc_rr(cpu, r_1, r_2):
    # inc rr
    # ––
    # [1] rr = rr+1 ; rr may be BC,DE,HL,SP
    value = (cpu.registers[r_1] << 8) + cpu.registers[r_2]
    value += 1
    cpu.registers[r_1] = value & 0xFF00
    cpu.registers[r_2] = value & 0x00FF


def dec_rr(cpu, r_1, r_2):
    # dec rr
    # ––
    # [1] rr = rr-1 ; rr may be BC,DE,HL,SP
    value = (cpu.registers[r_1] << 8) + cpu.registers[r_2]
    value -= 1
    cpu.registers[r_1] = value & 0xFF00
    cpu.registers[r_2] = value & 0x00FF


def add_spdd(cpu, n):
    # add SP,n
    # 00hc
    # [1] SP = SP +/- n
    flag = [0, 0, 0, 0, 0, 0, 0, 0]
    if (((cpu.sp & 0xf) + (n & 0xf)) & 0x10) == 0x10:
        flag[5] = 1
    cpu.sp += n
    if cpu.sp > 0xFFFF:
        cpu.sp -= (0xFFFF + 1)
        flag[4] = 1
    cpu.registers['F'] = lbin_to_hex(flag)


def ld_hlspdd(cpu, n):
    # ld HL,SP+dd
    # 00hc
    # [1] HL = SP +/- dd ; dd is 8-bit signed number
    flag = [0, 0, 0, 0, 0, 0, 0, 0]
    if (((cpu.sp & 0xf) + (n & 0xf)) & 0x10) == 0x10:
        flag[5] = 1
    value = cpu.sp + n
    if value > 0xFFFF:
        value -= (0xFFFF + 1)
        flag[4] = 1
    cpu.registers['H'] = value & 0xFF00
    cpu.registers['L'] = value & 0x00FF
