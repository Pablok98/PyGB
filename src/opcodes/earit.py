from utils import hex_to_lbin, lbin_to_hex


# ******   ADD   **********
def add_op(cpu, value, carry=False):
    if carry:
        carry = hex_to_lbin(cpu.registers['F'])[4]
        value += carry
    new_value = cpu.registers['A'] + value
    flag = [0, 0, 0, 0, 0, 0, 0, 0]
    if (((cpu.registers['A'] & 0xf) + (value & 0xf)) & 0x10) == 0x10:
        flag[5] = 1
    if new_value >= 256:
        new_value -= 256
        flag[4] = 1
    cpu.registers['A'] = new_value
    if new_value == 0:
        flag[7] = 1
    cpu.registers['F'] = lbin_to_hex(flag)


def add_ar(cpu, r):
    # Add A,r
    # z0hc
    add_op(cpu, cpu.registers[r])


def add_an(cpu, n):
    # Add A,n
    # z0hc
    add_op(cpu, n)


def add_ahl(cpu):
    # Add A,(HL)
    # z0hc
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = cpu.memory.read_data(first + second)
    add_op(cpu, value)


# ******   ADC   **********
def adc_ar(cpu, r):
    # adc A,r
    # z0hc
    add_op(cpu, cpu.registers[r], True)


def adc_an(cpu, n):
    # adc A,n
    # z0hc
    add_op(cpu, n, True)


def adc_ahl(cpu):
    # adc A,(HL)
    # z0hc
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = cpu.memory.read_data(first + second)
    add_op(cpu, value, True)


# ***  Subtraction  ****
def sub_op(cpu, value, carry=False):
    if carry:
        carry = hex_to_lbin(cpu.registers['F'])[4]
        value += carry
    new_value = cpu.registers['A'] - value
    flag = [0, 0, 0, 0, 0, 0, 1, 0]
    if (((cpu.registers['A'] & 0xf) - (value & 0xf)) & 0x10) == 0x10:
        flag[5] = 1
    if new_value < 0:
        new_value += 256
        flag[4] = 1
    cpu.registers['A'] = new_value
    if new_value == 0:
        flag[7] = 1
    cpu.registers['F'] = lbin_to_hex(flag)


def sub_ar(cpu, r):
    # sub A,r
    # z1hc
    sub_op(cpu, cpu.registers[r])


def sub_an(cpu, n):
    # sub A,n
    # z1hc
    sub_op(cpu, n)


def sub_ahl(cpu):
    # sub A,(HL)
    # z1hc
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = cpu.memory.read_data(first + second)
    sub_op(cpu, value)


def sbc_ar(cpu, r):
    # sbc A,r
    # z1hc
    sub_op(cpu, cpu.registers[r], True)


def sbc_an(cpu, n):
    # sbc A,n
    # z1hc
    sub_op(cpu, n, True)


def sbc_ahl(cpu):
    # sbc A,(HL)
    # z1hc
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = cpu.memory.read_data(first + second)
    sub_op(cpu, value, True)


# *********  AND  *********
def and_op(cpu, value):
    new_value = cpu.registers['A'] & value
    cpu.registers['A'] = new_value
    flag = [0, 0, 0, 0, 0, 1, 0, 0]
    if new_value == 0:
        flag[7] = 1
    cpu.registers['F'] = lbin_to_hex(flag)


def and_ar(cpu, r):
    # and A,r
    # z010
    and_op(cpu, cpu.registers[r])


def and_an(cpu, n):
    # and A,n
    # z010
    and_op(cpu, n)


def and_ahl(cpu):
    # and A,(HL)
    # z010
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = cpu.memory.read_data(first + second)
    and_op(cpu, value)


# *** XOR
def xor_op(cpu, value):
    new_value = cpu.registers['A'] ^ value
    cpu.registers['A'] = new_value
    flag = [0, 0, 0, 0, 0, 0, 0, 0]
    if new_value == 0:
        flag[7] = 1
    cpu.registers['F'] = lbin_to_hex(flag)


def xor_ar(cpu, r):
    # xor A,r
    # z000
    xor_op(cpu, cpu.registers[r])


def xor_an(cpu, n):
    # xor A,n
    # z000
    xor_op(cpu, n)


def xor_ahl(cpu):
    # xor A,(HL)
    # z000
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = cpu.memory.read_data(first + second)
    xor_op(cpu, value)


# *** OR
def or_op(cpu, value):
    new_value = cpu.registers['A'] | value
    cpu.registers['A'] = new_value
    flag = [0, 0, 0, 0, 0, 0, 0, 0]
    if new_value == 0:
        flag[7] = 1
    cpu.registers['F'] = lbin_to_hex(flag)


def or_ar(cpu, r):
    # or A,r
    # z000
    or_op(cpu, cpu.registers[r])


def or_an(cpu, n):
    # or A,n
    # z000
    or_op(cpu, n)


def or_ahl(cpu):
    # or A,(HL)
    # z000
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = cpu.memory.read_data(first + second)
    or_op(cpu, value)


# ****  Compare  ****
def cp_op(cpu, value):
    new_value = cpu.registers['A'] - value
    flag = [0, 0, 0, 0, 0, 0, 1, 0]
    if (((cpu.registers['A'] & 0xf) - (value & 0xf)) & 0x10) == 0x10:
        flag[5] = 1
    if new_value <= 0:
        new_value += 256
        flag[4] = 1
    if new_value == 0:
        flag[7] = 1
    cpu.registers['F'] = lbin_to_hex(flag)


def cp_ar(cpu, r):
    # cp A,r
    # z1hc
    cp_op(cpu, cpu.registers[r])


def cp_an(cpu, n):
    # cp A,n
    # z1hc
    cp_op(cpu, n)


def cp_ahl(cpu):
    # cp A,(HL)
    # z1hc
    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    value = cpu.memory.read_data(first + second)
    cp_op(cpu, value)


# ** OTHER **
def inc_r(cpu, r):
    # inc r
    # z0h-
    flag = hex_to_lbin(cpu.registers['F'])[4]
    flag = [0, 0, 0, 0, flag, 0, 0, 0]
    if (((cpu.registers[r] & 0xf) + (1 & 0xf)) & 0x10) == 0x10:
        flag[5] = 1
    cpu.registers[r] += 1
    if cpu.registers[r] >= 256:
        cpu.registers[r] -= 256
    if cpu.registers[r] == 0:
        flag[7] = 1
    cpu.registers['F'] = lbin_to_hex(flag)


def inc_hl(cpu):
    # inc (HL)
    # z0h-
    flag = hex_to_lbin(cpu.registers['F'])[4]
    flag = [0, 0, 0, 0, flag, 0, 0, 0]

    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    address = first + second
    value = cpu.memory.read_data(address)
    if (((value & 0xf) + (1 & 0xf)) & 0x10) == 0x10:
        flag[5] = 1
    value += 1
    if value >= 256:
        value -= 256
    if value == 0:
        flag[7] = 1
    cpu.memory.write_data(value, address)
    cpu.registers['F'] = lbin_to_hex(flag)


def dec_r(cpu, r):
    # dec r
    # z1h-
    flag = hex_to_lbin(cpu.registers['F'])[4]
    flag = [0, 0, 0, 0, flag, 0, 1, 0]
    if (((cpu.registers[r] & 0xf) - (1 & 0xf)) & 0x10) == 0x10:
        flag[5] = 1
    cpu.registers[r] -= 1
    if cpu.registers[r] < 0:
        cpu.registers[r] += 256
    if cpu.registers[r] == 0:
        flag[7] = 1
    cpu.registers['F'] = lbin_to_hex(flag)


def dec_hl(cpu):
    # dec (HL)
    # z1h-
    flag = hex_to_lbin(cpu.registers['F'])[4]
    flag = [0, 0, 0, 0, flag, 0, 1, 0]

    first = (cpu.registers['H'] << 8) & 0xFF00
    second = cpu.registers['L']
    address = first + second
    value = cpu.memory.read_data(address)
    if (((value & 0xf) - (1 & 0xf)) & 0x10) == 0x10:
        flag[5] = 1
    value -= 1
    if value < 0:
        value += 256
    if value == 0:
        flag[7] = 1
    cpu.memory.write_data(value, address)
    cpu.registers['F'] = lbin_to_hex(flag)


def daa(cpu):
    # daa
    # z-0c
    pass


def cpl(cpu):
    # cpl
    # -11-
    pass