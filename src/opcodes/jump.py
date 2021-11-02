def jump_nn(cpu, n_1, n_2):
    # jp nn
    pass


def jump_hl(cpu):
    # jp HL
    pass


def jump_fnn(cpu, cond, nn):
    # jp f,nn
    pass


def jumpr_pcdd(cpu, d):
    # jr PC+dd
    pass


def jr_fpcdd(cpu, cond, d):
    # jr f,PC+dd
    pass


def call_nn(cpu, nn_1, nn_2):
    # call nn
    pass


def call_fnn(cpu, cond, nn_1, nn_2):
    # call f,nn
    pass


def ret(cpu):
    # ret
    pass


def retf(cpu, cond):
    # ret f
    pass


def reti(cpu):
    # reti
    pass


def rst_n(cpu, n):
    # rst n
    pass