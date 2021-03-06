from collections import namedtuple
from . import earit as ea
from . import sarit as sa
from . import eload as el
from . import sload as sl
from . import rotshi as rot
from . import sbop as sb
from . import jump as jp
from . import cpu_ctrl as ctrl
from . import rotshi as rs
Opc = namedtuple("Opcode", ['mnemonic', 'cycl', 'len', 'func', 'args'])


def mock(cpu):
    return


pointer = {
    0x00: Opc('NOP', 4, 1, ctrl.nop, []),
    0x01: Opc('LD BC,nn', 12, 3, sl.load_rrnn, ['B', 'C']),
    0x02: Opc('LD (BC),A', 8, 1, el.load_hlr, ['B', 'C', 'A']),
    0x03: Opc('INC BC', 8, 1, sa.inc_rr, ['B', 'C']),
    0x04: Opc('INC B', 4, 1, ea.inc_r, ['B']),
    0x05: Opc('DEC B', 4, 1, ea.dec_r, ['B']),
    0x06: Opc('LD B,n', 8, 2, el.load_rn, ['B']),
    0x07: Opc('RLCA', 4, 1, rs.rlca, []),
    0x08: Opc('LD (nn),SP', 20, 3, sl.load_nnsp, []),
    0x09: Opc('ADD HL,BC', 8, 1, sa.add_hlrr, ['B', 'C']),
    0x0A: Opc('LD A,(BC)', 8, 1, el.load_rhl, ['A', 'B', 'C']),
    0x0B: Opc('DEC BC', 8, 1, sa.dec_rr, ['B', 'C']),
    0x0C: Opc('INC C', 4, 1, ea.inc_r, ['B']),
    0x0D: Opc('DEC C', 4, 1, ea.dec_r, ['C']),
    0x0E: Opc('LD C,n', 8, 2, el.load_rn, ['C']),
    0x0F: Opc('RRCA', 4, 1, rs.rrca, []),
    0x10: Opc('STOP', 4, 2, ctrl.halt, []),
    0x11: Opc('LD DE,nn', 12, 3, sl.load_rrnn, ['D', 'E']),
    0x12: Opc('LD (DE),A', 8, 1, el.load_hlr, ['D', 'E', 'A']),
    0x13: Opc('INC DE', 8, 1, sa.inc_rr, ['D', 'E']),
    0x14: Opc('INC D', 4, 1, ea.inc_r, ['D']),
    0x15: Opc('DEC D', 4, 1, ea.dec_r, ['D']),
    0x16: Opc('LD D,n', 8, 2, el.load_rn, ['D']),
    0x17: Opc('RLA', 4, 1, rs.rla, []),
    0x18: Opc('JR n', 12, 2, jp.jumpr_pcdd, []),
    0x19: Opc('ADD HL,DE', 8, 1, sa.add_hlrr, ['D', 'E']),
    0x1A: Opc('LD A,(DE)', 8, 1, el.load_rhl, ['A', 'D', 'E']),
    0x1B: Opc('DEC DE', 8, 1, sa.dec_rr, ['D', 'E']),
    0x1C: Opc('INC E', 4, 1, ea.inc_r, ['E']),
    0x1D: Opc('DEC E', 4, 1, ea.dec_r, ['E']),
    0x1E: Opc('LD E,n', 8, 2, el.load_rn, ['E']),
    0x1F: Opc('RRA', 4, 1, rs.rra, []),
    0x20: Opc('JR NZ,nn', 8, 2, jp.jr_fpcdd, ['NZ']),
    0x21: Opc('LD HL,nn', 12, 3, sl.load_rrnn, ['H', 'L']),
    0x22: Opc('LD (HL+),A', 8, 1, el.load_igla, []),
    0x23: Opc('INC HL', 8, 1, sa.inc_rr, ['H', 'L']),
    0x24: Opc('INC H', 4, 1, ea.inc_r, ['H']),
    0x25: Opc('DEC H', 4, 1, ea.dec_r, ['H']),
    0x26: Opc('LD H,n', 8, 2, el.load_rn, ['H']),
    0x27: Opc('DAA', 4, 1, ea.daa, []),
    0x28: Opc('JR Z,nn', 8, 2, jp.jr_fpcdd, ['Z']),
    0x29: Opc('ADD HL,HL', 8, 1, sa.add_hlrr, ['H', 'L']),
    0x2A: Opc('LD A,(HL+)', 8, 1, el.load_iahl, []),
    0x2B: Opc('DEC HL', 8, 1, sa.dec_rr, ['H', 'L']),
    0x2C: Opc('INC L', 4, 1, ea.inc_r, ['L']),
    0x2D: Opc('DEC L', 4, 1, ea.dec_r, ['L']),
    0x2E: Opc('LD L,n', 8, 2, el.load_rn, ['L']),
    0x2F: Opc('CPL', 4, 1, ea.cpl, []),
    0x30: Opc('JR NC,nn', 8, 2, jp.jr_fpcdd, ['NC']),
    # TODO: SP is 16-bit, make property
    0x31: Opc('LD SP,nn', 12, 3, sl.load_rrnn, ['S', 'P']),
    0x32: Opc('LD (HL-),A', 8, 1, el.load_dgla, []),
    0x33: Opc('INC SP', 8, 1, sa.inc_rr, ['S', 'P']),
    0x34: Opc('INC (HL)', 12, 1, ea.inc_hl, []),
    0x35: Opc('DEC (HL)', 12, 1,  ea.dec_hl, []),
    0x36: Opc('LD (HL),n', 12, 2, el.load_RRn, ['H', 'L']),
    0x37: Opc('SCF', 4, 1, ctrl.scf, []),
    0x38: Opc('JR C,n', 8, 2, jp.jr_fpcdd, ['C']),
    0x39: Opc('ADD HL,SP', 8, 1, sa.add_hlrr, ['S', 'P']),
    0x3A: Opc('LD A,(HL-)', 8, 1, el.load_dahl, []),
    0x3B: Opc('DEC SP', 8, 1, sa.dec_rr, ['S', 'P']),
    0x3C: Opc('INC A', 4, 1, ea.inc_r, ['A']),
    0x3D: Opc('DEC A', 4, 1, ea.dec_r, ['A']),
    0x3E: Opc('LD A,n', 8, 2, el.load_rn, ['A']),
    0x3F: Opc('CCF', 4, 1, ctrl.ccf, []),
    0x40: Opc('LD B,B', 4, 1, el.load_rr, ['B', 'B']),
    0x41: Opc('LD B,C', 4, 1, el.load_rr, ['B', 'C']),
    0x42: Opc('LD B,D', 4, 1, el.load_rr, ['B', 'D']),
    0x43: Opc('LD B,E', 4, 1, el.load_rr, ['B', 'E']),
    0x44: Opc('LD B,H', 4, 1, el.load_rr, ['B', 'H']),
    0x45: Opc('LD B,L', 4, 1, el.load_rr, ['B', 'L']),
    0x46: Opc('LD B,(HL)', 8, 1, el.load_rhl, ['B', 'H', 'L']),
    0x47: Opc('LD B,A', 4, 1, el.load_rr, ['B', 'A']),
    0x48: Opc('LD C,B', 4, 1, el.load_rr, ['C', 'B']),
    0x49: Opc('LD C,C', 4, 1, el.load_rr, ['C', 'C']),
    0x4A: Opc('LD C,D', 4, 1, el.load_rr, ['C', 'D']),
    0x4B: Opc('LD C,E', 4, 1, el.load_rr, ['C', 'E']),
    0x4C: Opc('LD C,H', 4, 1, el.load_rr, ['C', 'H']),
    0x4D: Opc('LD C,L', 4, 1, el.load_rr, ['C', 'L']),
    0x4E: Opc('LD C,(HL)', 8, 1, el.load_rhl, ['A', 'H', 'L']),
    0x4F: Opc('LD C,A', 4, 1, el.load_rr, ['C', 'A']),
    0x50: Opc('LD D,B', 4, 1, el.load_rr, ['D', 'B']),
    0x51: Opc('LD D,C', 4, 1, el.load_rr, ['D', 'C']),
    0x52: Opc('LD D,D', 4, 1, el.load_rr, ['D', 'D']),
    0x53: Opc('LD D,E', 4, 1, el.load_rr, ['D', 'E']),
    0x54: Opc('LD D,H', 4, 1, el.load_rr, ['D', 'H']),
    0x55: Opc('LD D,L', 4, 1, el.load_rr, ['D', 'L']),
    0x56: Opc('LD D,(HL)', 8, 1, el.load_rhl, ['D', 'H', 'L']),
    0x57: Opc('LD D,A', 4, 1, el.load_rr, ['D', 'A']),
    0x58: Opc('LD E,B', 4, 1, el.load_rr, ['E', 'B']),
    0x59: Opc('LD E,C', 4, 1, el.load_rr, ['E', 'C']),
    0x5A: Opc('LD E,D', 4, 1, el.load_rr, ['E', 'D']),
    0x5B: Opc('LD E,E', 4, 1, el.load_rr, ['E', 'E']),
    0x5C: Opc('LD E,H', 4, 1, el.load_rr, ['E', 'H']),
    0x5D: Opc('LD E,L', 4, 1, el.load_rr, ['E', 'L']),
    0x5E: Opc('LD E,(HL)', 8, 1, el.load_rhl, ['E', 'H', 'L']),
    0x5F: Opc('LD E,A', 4, 1, el.load_rr, ['E', 'A']),
    0x60: Opc('LD H,B', 4, 1, el.load_rr, ['H', 'B']),
    0x61: Opc('LD H,C', 4, 1, el.load_rr, ['H', 'C']),
    0x62: Opc('LD H,D', 4, 1, el.load_rr, ['H', 'D']),
    0x63: Opc('LD H,E', 4, 1, el.load_rr, ['H', 'E']),
    0x64: Opc('LD H,H', 4, 1, el.load_rr, ['H', 'H']),
    0x65: Opc('LD H,L', 4, 1, el.load_rr, ['H', 'L']),
    0x66: Opc('LD H,(HL)', 8, 1, el.load_rhl, ['H', 'H', 'L']),
    0x67: Opc('LD H,A', 4, 1, el.load_rr, ['H', 'A']),
    0x68: Opc('LD L,B', 4, 1, el.load_rr, ['L', 'B']),
    0x69: Opc('LD L,C', 4, 1, el.load_rr, ['L', 'C']),
    0x6A: Opc('LD L,D', 4, 1, el.load_rr, ['L', 'D']),
    0x6B: Opc('LD L,E', 4, 1, el.load_rr, ['L', 'E']),
    0x6C: Opc('LD L,H', 4, 1, el.load_rr, ['L', 'H']),
    0x6D: Opc('LD L,L', 4, 1, el.load_rr, ['L', 'L']),
    0x6E: Opc('LD L,(HL)', 8, 1, el.load_rhl, ['L', 'H', 'L']),
    0x6F: Opc('LD L,A', 4, 1, el.load_rr, ['L', 'A']),
    0x70: Opc('LD (HL),B', 8, 1, el.load_hlr, ['H', 'L', 'B']),
    0x71: Opc('LD (HL),C', 8, 1, el.load_hlr, ['H', 'L', 'C']),
    0x72: Opc('LD (HL),D', 8, 1, el.load_hlr, ['H', 'L', 'D']),
    0x73: Opc('LD (HL),E', 8, 1, el.load_hlr, ['H', 'L', 'E']),
    0x74: Opc('LD (HL),H', 8, 1, el.load_hlr, ['H', 'L', 'H']),
    0x75: Opc('LD (HL),L', 8, 1, el.load_hlr, ['H', 'L', 'L']),
    0x76: Opc('HALT', 4, 1, ctrl.halt, []),
    0x77: Opc('LD (HL),A', 8, 1, el.load_hlr, ['H', 'L', 'A']),
    0x78: Opc('LD A,B', 4, 1, el.load_rr, ['A', 'B']),
    0x79: Opc('LD A,C', 4, 1, el.load_rr, ['A', 'C']),
    0x7A: Opc('LD A,D', 4, 1, el.load_rr, ['A', 'D']),
    0x7B: Opc('LD A,E', 4, 1, el.load_rr, ['A', 'E']),
    0x7C: Opc('LD A,H', 4, 1, el.load_rr, ['A', 'H']),
    0x7D: Opc('LD A,L', 4, 1, el.load_rr, ['A', 'L']),
    0x7E: Opc('LD A,(HL)', 8, 1, el.load_rhl, ['A', 'H', 'L']),
    0x7F: Opc('LD A,A', 4, 1,  el.load_rr, ['A', 'A']),
    0x80: Opc('ADD A,B', 4, 1, ea.add_ar, ['B']),
    0x81: Opc('ADD A,C', 4, 1, ea.add_ar, ['C']),
    0x82: Opc('ADD A,D', 4, 1, ea.add_ar, ['D']),
    0x83: Opc('ADD A,E', 4, 1, ea.add_ar, ['E']),
    0x84: Opc('ADD A,H', 4, 1, ea.add_ar, ['H']),
    0x85: Opc('ADD A,L', 4, 1, ea.add_ar, ['L']),
    0x86: Opc('ADD A,(HL)', 8, 1, ea.add_ahl, ['H', 'L']),
    0x87: Opc('ADD A,A', 4, 1, ea.add_ar, ['A']),
    0x88: Opc('ADC A,B', 4, 1, ea.adc_ar, ['B']),
    0x89: Opc('ADC A,C', 4, 1, ea.adc_ar, ['C']),
    0x8A: Opc('ADC A,D', 4, 1, ea.adc_ar, ['D']),
    0x8B: Opc('ADC A,E', 4, 1, ea.adc_ar, ['E']),
    0x8C: Opc('ADC A,H', 4, 1, ea.adc_ar, ['H']),
    0x8D: Opc('ADC A,L', 4, 1, ea.adc_ar, ['L']),
    0x8E: Opc('ADC A,(HL)', 8, 1, ea.adc_ahl, []),
    0x8F: Opc('ADC A,A', 4, 1, ea.adc_ar, ['A']),
    0x90: Opc('SUB A,B', 4, 1, ea.sub_ar, ['B']),
    0x91: Opc('SUB A,C', 4, 1, ea.sub_ar, ['C']),
    0x92: Opc('SUB A,D', 4, 1, ea.sub_ar, ['D']),
    0x93: Opc('SUB A,E', 4, 1, ea.sub_ar, ['E']),
    0x94: Opc('SUB A,H', 4, 1, ea.sub_ar, ['H']),
    0x95: Opc('SUB A,L', 4, 1, ea.sub_ar, ['L']),
    0x96: Opc('SUB A,(HL)', 8, 1, ea.sub_ahl, []),
    0x97: Opc('SUB A,A', 4, 1, ea.sub_ar, ['A']),
    0x98: Opc('SBC A,B', 4, 1, ea.sbc_ar, ['B']),
    0x99: Opc('SBC A,C', 4, 1, ea.sbc_ar, ['C']),
    0x9A: Opc('SBC A,D', 4, 1, ea.sbc_ar, ['D']),
    0x9B: Opc('SBC A,E', 4, 1, ea.sbc_ar, ['E']),
    0x9C: Opc('SBC A,H', 4, 1, ea.sbc_ar, ['H']),
    0x9D: Opc('SBC A,L', 4, 1, ea.sbc_ar, ['L']),
    0x9E: Opc('SBC A,(HL)', 8, 1, ea.sub_ahl, []),
    0x9F: Opc('SBC A,A', 4, 1, ea.sbc_ar, ['A']),
    0xA0: Opc('AND A,B', 4, 1, ea.and_ar, ['B']),
    0xA1: Opc('AND A,C', 4, 1, ea.and_ar, ['C']),
    0xA2: Opc('AND A,D', 4, 1, ea.and_ar, ['D']),
    0xA3: Opc('AND A,E', 4, 1, ea.and_ar, ['E']),
    0xA4: Opc('AND A,H', 4, 1, ea.and_ar, ['H']),
    0xA5: Opc('AND A,L', 4, 1, ea.and_ar, ['L']),
    0xA6: Opc('AND A,(HL)', 8, 1, ea.and_ahl, []),
    0xA7: Opc('AND A,A', 4, 1, ea.and_ar, ['A']),
    0xA8: Opc('XOR A,B', 4, 1, ea.xor_ar, ['B']),
    0xA9: Opc('XOR A,C', 4, 1, ea.xor_ar, ['C']),
    0xAA: Opc('XOR A,D', 4, 1, ea.xor_ar, ['D']),
    0xAB: Opc('XOR A,E', 4, 1, ea.xor_ar, ['E']),
    0xAC: Opc('XOR A,H', 4, 1, ea.xor_ar, ['H']),
    0xAD: Opc('XOR A,L', 4, 1, ea.xor_ar, ['L']),
    0xAE: Opc('XOR A,(HL)', 8, 1, ea.xor_ahl, []),
    0xAF: Opc('XOR A,A', 4, 1, ea.xor_ar, ['A']),
    0xB0: Opc('OR A,B', 4, 1, ea.or_ar, ['B']),
    0xB1: Opc('OR A,C', 4, 1, ea.or_ar, ['C']),
    0xB2: Opc('OR A,D', 4, 1, ea.or_ar, ['D']),
    0xB3: Opc('OR A,E', 4, 1, ea.or_ar, ['E']),
    0xB4: Opc('OR A,H', 4, 1, ea.or_ar, ['H']),
    0xB5: Opc('OR A,L', 4, 1, ea.or_ar, ['L']),
    0xB6: Opc('OR A,(HL)', 8, 1, ea.or_ahl, []),
    0xB7: Opc('OR A,A', 4, 1, ea.or_ar, ['A']),
    0xB8: Opc('CP A,B', 4, 1, ea.cp_ar, ['B']),
    0xB9: Opc('CP A,C', 4, 1, ea.cp_ar, ['C']),
    0xBA: Opc('CP A,D', 4, 1, ea.cp_ar, ['D']),
    0xBB: Opc('CP A,E', 4, 1, ea.cp_ar, ['E']),
    0xBC: Opc('CP A,H', 4, 1, ea.cp_ar, ['H']),
    0xBD: Opc('CP A,L', 4, 1, ea.cp_ar, ['L']),
    0xBE: Opc('CP A,(HL)', 8, 1, ea.cp_ahl, []),
    0xBF: Opc('CP A,A', 4, 1, ea.cp_ar, ['A']),
    0xC0: Opc('RET NZ', 8, 1, jp.retf, ['NZ']),
    0xC1: Opc('POP BC', 12, 1, sl.pop_rr, ['B', 'C']),
    0xC2: Opc('JP NZ,nn', 12, 3, jp.jump_fnn, ['NZ']),
    0xC3: Opc('JP nn', 16, 3, jp.jump_nn, []),
    0xC4: Opc('CALL NZ,nn', 12, 3, jp.call_fnn, ['NZ']),
    0xC5: Opc('PUSH BC', 16, 1, sl.push_rr, ['B', 'C']),
    0xC6: Opc('ADD A,n', 8, 2, ea.add_an, []),
    0xC7: Opc('RST 00h', 16, 1, jp.rst_n, ['00']),
    0xC8: Opc('RET Z', 8, 1, jp.retf, ['Z']),
    0xC9: Opc('RET', 16, 1, jp.ret, []),
    0xCA: Opc('JP Z,nn', 12, 3, jp.jump_fnn, ['Z']),
    0xCB: Opc('PREFIX CB', 4, 1, mock, []),
    0xCC: Opc('CALL Z,nn', 12, 3, jp.call_fnn, ['Z']),
    0xCD: Opc('CALL nn', 24, 3, jp.call_nn, []),
    0xCE: Opc('ADC A,n', 8, 2, ea.adc_an, []),
    0xCF: Opc('RST 08h', 16, 1, jp.rst_n, ['08']),
    0xD0: Opc('RET NC', 8, 1, jp.retf, ['NC']),
    0xD1: Opc('POP DE', 12, 1, sl.pop_rr, ['D', 'E']),
    0xD2: Opc('JP NC,nn', 12, 3, jp.jump_fnn, ['NC']),
    0xD4: Opc('CALL NC,nn', 12, 3, jp.call_fnn, ['NC']),
    0xD5: Opc('PUSH DE', 16, 1, sl.push_rr, ['D', 'E']),
    0xD6: Opc('SUB A,n', 8, 2, ea.sub_an, []),
    0xD7: Opc('RST 10h', 16, 1, jp.rst_n, ['10']),
    0xD8: Opc('RET C', 8, 1, jp.retf, ['C']),
    0xD9: Opc('RETI', 16, 1, jp.reti, []),
    0xDA: Opc('JP C,nn', 12, 3, jp.jump_fnn, ['C']),
    0xDC: Opc('CALL C,nn', 12, 3, jp.call_fnn, ['C']),
    0xDE: Opc('SBC A,n', 8, 2, ea.sbc_an, []),
    0xDF: Opc('RST 18h', 16, 1, jp.rst_n, ['18']),
    0xE0: Opc('LD (FF00+n),A', 12, 2, el.ld_ioto, []),
    0xE1: Opc('POP HL', 12, 1, sl.pop_rr, ['H', 'L']),
    0xE2: Opc('LD (FF00+C),A', 8, 1, el.ld_iotoc, []),
    0xE5: Opc('PUSH HL', 16, 1, sl.push_rr, ['H', 'L']),
    0xE6: Opc('AND A,n', 8, 2, ea.and_an, []),
    0xE7: Opc('RST 20h', 16, 1, jp.rst_n, ['20']),
    0xE8: Opc('ADD SP,n', 16, 2, sa.add_spdd, []),
    0xE9: Opc('JP HL', 4, 1, jp.jump_hl, []),
    0xEA: Opc('LD (nn),A', 16, 3, el.load_nnR, ['A']),
    0xEE: Opc('XOR A,n', 8, 2, ea.xor_an, []),
    0xEF: Opc('RST 28h', 16, 1, jp.rst_n, ['28']),
    0xF0: Opc('LD A,(FF00+n)', 12, 2, el.ld_iofrom, []),
    0xF1: Opc('POP AF', 12, 1, sl.pop_rr, ['A', 'F']),
    0xF2: Opc('LD A,(FF00+C)', 8, 1, el.ld_iofromc, []),
    0xF3: Opc('DI', 4, 1, ctrl.di, []),
    0xF5: Opc('PUSH AF', 1, 16,  sl.push_rr, ['A', 'F']),
    0xF6: Opc('OR A,n', 8, 2, ea.or_an, []),
    0xF7: Opc('RST 30h', 16, 1, jp.rst_n, ['30']),
    0xF8: Opc('LD HL,SP+n', 12, 2, sa.ld_hlspdd, []),
    0xF9: Opc('LD SP,HL', 8, 1, sl.load_sphl, []),
    0xFA: Opc('LD A,(nn)', 16, 3, el.load_Rnn, ['A']),
    0xFB: Opc('EI', 4, 1, ctrl.ei, []),
    0xFE: Opc('CP A,n', 8, 2, ea.cp_an, []),
    0xFF: Opc('RST 38h', 16, 1, jp.rst_n, ['38']),
}

cb_pointer = {
    0x00: Opc('RLC B', 8, 2, rot.rlc_r, ['B']),
    0x01: Opc('RLC C', 8, 2, rot.rlc_r, ['C']),
    0x02: Opc('RLC D', 8, 2, rot.rlc_r, ['D']),
    0x03: Opc('RLC E', 8, 2, rot.rlc_r, ['E']),
    0x04: Opc('RLC H', 8, 2, rot.rlc_r, ['H']),
    0x05: Opc('RLC L', 8, 2, rot.rlc_r, ['L']),
    0x06: Opc('RLC (HL)', 16, 2, rot.rlc_hl, []),
    0x07: Opc('RLC A', 8, 2, rot.rlc_r, ['A']),
    0x08: Opc('RRC B', 8, 2, rot.rrc_r, ['B']),
    0x09: Opc('RRC C', 8, 2, rot.rrc_r, ['C']),
    0x0A: Opc('RRC D', 8, 2, rot.rrc_r, ['D']),
    0x0B: Opc('RRC E', 8, 2, rot.rrc_r, ['E']),
    0x0C: Opc('RRC H', 8, 2, rot.rrc_r, ['H']),
    0x0D: Opc('RRC L', 8, 2, rot.rrc_r, ['L']),
    0x0E: Opc('RRC (HL)', 16, 2, rot.rrc_hl, []),
    0x0F: Opc('RRC A', 8, 2, rot.rrc_r, ['A']),
    0x10: Opc('RL B', 8, 2, rot.rl_r, ['B']),
    0x11: Opc('RL C', 8, 2, rot.rl_r, ['C']),
    0x12: Opc('RL D', 8, 2, rot.rl_r, ['D']),
    0x13: Opc('RL E', 8, 2, rot.rl_r, ['E']),
    0x14: Opc('RL H', 8, 2, rot.rl_r, ['H']),
    0x15: Opc('RL L', 8, 2, rot.rl_r, ['L']),
    0x16: Opc('RL (HL)', 16, 2, rot.rl_hl, []),
    0x17: Opc('RL A', 8, 2, rot.rl_r, ['A']),
    0x18: Opc('RR B', 8, 2, rot.rr_r, ['B']),
    0x19: Opc('RR C', 8, 2, rot.rr_r, ['C']),
    0x1A: Opc('RR D', 8, 2, rot.rr_r, ['D']),
    0x1B: Opc('RR E', 8, 2, rot.rr_r, ['E']),
    0x1C: Opc('RR H', 8, 2, rot.rr_r, ['H']),
    0x1D: Opc('RR L', 8, 2, rot.rr_r, ['L']),
    0x1E: Opc('RR (HL)', 16, 2, rot.rr_hl, []),
    0x1F: Opc('RR A', 8, 2, rot.rr_r, ['A']),
    0x20: Opc('SLA B', 8, 2, rot.sla_r, ['B']),
    0x21: Opc('SLA C', 8, 2, rot.sla_r, ['C']),
    0x22: Opc('SLA D', 8, 2, rot.sla_r, ['D']),
    0x23: Opc('SLA E', 8, 2, rot.sla_r, ['E']),
    0x24: Opc('SLA H', 8, 2, rot.sla_r, ['H']),
    0x25: Opc('SLA L', 8, 2, rot.sla_r, ['L']),
    0x26: Opc('SLA (HL)', 16, 2, rot.sla_hl, []),
    0x27: Opc('SLA A', 8, 2, rot.sla_r, ['A']),
    0x28: Opc('SRA B', 8, 2, rot.sra_r, ['B']),
    0x29: Opc('SRA C', 8, 2, rot.sra_r, ['C']),
    0x2A: Opc('SRA D', 8, 2, rot.sra_r, ['D']),
    0x2B: Opc('SRA E', 8, 2, rot.sra_r, ['E']),
    0x2C: Opc('SRA H', 8, 2, rot.sra_r, ['H']),
    0x2D: Opc('SRA L', 8, 2, rot.sra_r, ['L']),
    0x2E: Opc('SRA (HL)', 16, 2, rot.sra_hl, []),
    0x2F: Opc('SRA A', 8, 2, rot.sra_r, ['A']),
    0x30: Opc('SWAP B', 8, 2, rot.swap_r, ['B']),
    0x31: Opc('SWAP C', 8, 2, rot.swap_r, ['C']),
    0x32: Opc('SWAP D', 8, 2, rot.swap_r, ['D']),
    0x33: Opc('SWAP E', 8, 2, rot.swap_r, ['E']),
    0x34: Opc('SWAP H', 8, 2, rot.swap_r, ['H']),
    0x35: Opc('SWAP L', 8, 2, rot.swap_r, ['L']),
    0x36: Opc('SWAP (HL)', 16, 2, rot.swap_hl, []),
    0x37: Opc('SWAP A', 8, 2, rot.swap_r, ['A']),
    0x38: Opc('SRL B', 8, 2, rot.srl_r, ['B']),
    0x39: Opc('SRL C', 8, 2, rot.srl_r, ['C']),
    0x3A: Opc('SRL D', 8, 2, rot.srl_r, ['D']),
    0x3B: Opc('SRL E', 8, 2, rot.srl_r, ['E']),
    0x3C: Opc('SRL H', 8, 2, rot.srl_r, ['H']),
    0x3D: Opc('SRL L', 8, 2, rot.srl_r, ['L']),
    0x3E: Opc('SRL (HL)', 16, 2, rot.sra_hl, []),
    0x3F: Opc('SRL A', 8, 2, rot.srl_r, ['A']),
    0x40: Opc('BIT 0,B', 8, 2, sb.bit_nr, [0, 'B']),
    0x41: Opc('BIT 0,C', 8, 2, sb.bit_nr, [0, 'C']),
    0x42: Opc('BIT 0,D', 8, 2, sb.bit_nr, [0, 'D']),
    0x43: Opc('BIT 0,E', 8, 2, sb.bit_nr, [0, 'E']),
    0x44: Opc('BIT 0,H', 8, 2, sb.bit_nr, [0, 'H']),
    0x45: Opc('BIT 0,L', 8, 2, sb.bit_nr, [0, 'L']),
    0x46: Opc('BIT 0,(HL)', 12, 2, sb.bit_nhl, [0]),
    0x47: Opc('BIT 0,A', 8, 2, sb.bit_nr, [0, 'A']),
    0x48: Opc('BIT 1,B', 8, 2, sb.bit_nr, [1, 'B']),
    0x49: Opc('BIT 1,C', 8, 2, sb.bit_nr, [1, 'C']),
    0x4A: Opc('BIT 1,D', 8, 2, sb.bit_nr, [1, 'D']),
    0x4B: Opc('BIT 1,E', 8, 2, sb.bit_nr, [1, 'E']),
    0x4C: Opc('BIT 1,H', 8, 2, sb.bit_nr, [1, 'H']),
    0x4D: Opc('BIT 1,L', 8, 2, sb.bit_nr, [1, 'L']),
    0x4E: Opc('BIT 1,(HL)', 12, 2, sb.bit_nhl, [1]),
    0x4F: Opc('BIT 1,A', 8, 2, sb.bit_nr, [1, 'A']),
    0x50: Opc('BIT 2,B', 8, 2, sb.bit_nr, [2, 'B']),
    0x51: Opc('BIT 2,C', 8, 2, sb.bit_nr, [2, 'C']),
    0x52: Opc('BIT 2,D', 8, 2, sb.bit_nr, [2, 'D']),
    0x53: Opc('BIT 2,E', 8, 2, sb.bit_nr, [2, 'E']),
    0x54: Opc('BIT 2,H', 8, 2, sb.bit_nr, [2, 'H']),
    0x55: Opc('BIT 2,L', 8, 2, sb.bit_nr, [2, 'L']),
    0x56: Opc('BIT 2,(HL)', 12, 2, sb.bit_nhl, [2]),
    0x57: Opc('BIT 2,A', 8, 2, sb.bit_nr, [2, 'A']),
    0x58: Opc('BIT 3,B', 8, 2, sb.bit_nr, [3, 'B']),
    0x59: Opc('BIT 3,C', 8, 2, sb.bit_nr, [3, 'C']),
    0x5A: Opc('BIT 3,D', 8, 2, sb.bit_nr, [3, 'D']),
    0x5B: Opc('BIT 3,E', 8, 2, sb.bit_nr, [3, 'E']),
    0x5C: Opc('BIT 3,H', 8, 2, sb.bit_nr, [3, 'H']),
    0x5D: Opc('BIT 3,L', 8, 2, sb.bit_nr, [3, 'L']),
    0x5E: Opc('BIT 3,(HL)', 12, 2, sb.bit_nhl, [3]),
    0x5F: Opc('BIT 3,A', 8, 2, sb.bit_nr, [3, 'A']),
    0x60: Opc('BIT 4,B', 8, 2, sb.bit_nr, [4, 'B']),
    0x61: Opc('BIT 4,C', 8, 2, sb.bit_nr, [4, 'C']),
    0x62: Opc('BIT 4,D', 8, 2, sb.bit_nr, [4, 'D']),
    0x63: Opc('BIT 4,E', 8, 2, sb.bit_nr, [4, 'E']),
    0x64: Opc('BIT 4,H', 8, 2, sb.bit_nr, [4, 'H']),
    0x65: Opc('BIT 4,L', 8, 2, sb.bit_nr, [4, 'L']),
    0x66: Opc('BIT 4,(HL)', 12, 2, sb.bit_nhl, [4]),
    0x67: Opc('BIT 4,A', 8, 2, sb.bit_nr, [4, 'A']),
    0x68: Opc('BIT 5,B', 8, 2, sb.bit_nr, [5, 'B']),
    0x69: Opc('BIT 5,C', 8, 2, sb.bit_nr, [5, 'C']),
    0x6A: Opc('BIT 5,D', 8, 2, sb.bit_nr, [5, 'D']),
    0x6B: Opc('BIT 5,E', 8, 2, sb.bit_nr, [5, 'E']),
    0x6C: Opc('BIT 5,H', 8, 2, sb.bit_nr, [5, 'H']),
    0x6D: Opc('BIT 5,L', 8, 2, sb.bit_nr, [5, 'L']),
    0x6E: Opc('BIT 5,(HL)', 12, 2, sb.bit_nhl, [5]),
    0x6F: Opc('BIT 5,A', 8, 2, sb.bit_nr, [5, 'A']),
    0x70: Opc('BIT 6,B', 8, 2, sb.bit_nr, [6, 'B']),
    0x71: Opc('BIT 6,C', 8, 2, sb.bit_nr, [6, 'C']),
    0x72: Opc('BIT 6,D', 8, 2, sb.bit_nr, [6, 'D']),
    0x73: Opc('BIT 6,E', 8, 2, sb.bit_nr, [6, 'E']),
    0x74: Opc('BIT 6,H', 8, 2, sb.bit_nr, [6, 'H']),
    0x75: Opc('BIT 6,L', 8, 2, sb.bit_nr, [6, 'L']),
    0x76: Opc('BIT 6,(HL)', 12, 2, sb.bit_nhl, [6]),
    0x77: Opc('BIT 6,A', 8, 2, sb.bit_nr, [6, 'A']),
    0x78: Opc('BIT 7,B', 8, 2, sb.bit_nr, [7, 'B']),
    0x79: Opc('BIT 7,C', 8, 2, sb.bit_nr, [7, 'C']),
    0x7A: Opc('BIT 7,D', 8, 2, sb.bit_nr, [7, 'D']),
    0x7B: Opc('BIT 7,E', 8, 2, sb.bit_nr, [7, 'E']),
    0x7C: Opc('BIT 7,H', 8, 2, sb.bit_nr, [7, 'H']),
    0x7D: Opc('BIT 7,L', 8, 2, sb.bit_nr, [7, 'L']),
    0x7E: Opc('BIT 7,(HL)', 12, 2, sb.bit_nhl, [7]),
    0x7F: Opc('BIT 7,A', 8, 2, sb.bit_nr, [7, 'A']),
    0x80: Opc('RES 0,B', 8, 2, sb.res_nr, [0, 'B']),
    0x81: Opc('RES 0,C', 8, 2, sb.res_nr, [0, 'C']),
    0x82: Opc('RES 0,D', 8, 2, sb.res_nr, [0, 'D']),
    0x83: Opc('RES 0,E', 8, 2, sb.res_nr, [0, 'E']),
    0x84: Opc('RES 0,H', 8, 2, sb.res_nr, [0, 'H']),
    0x85: Opc('RES 0,L', 8, 2, sb.res_nr, [0, 'L']),
    0x86: Opc('RES 0,(HL)', 16, 2, sb.res_nhl, [0]),
    0x87: Opc('RES 0,A', 8, 2, sb.res_nr, [0, 'A']),
    0x88: Opc('RES 1,B', 8, 2, sb.res_nr, [1, 'B']),
    0x89: Opc('RES 1,C', 8, 2, sb.res_nr, [1, 'C']),
    0x8A: Opc('RES 1,D', 8, 2, sb.res_nr, [1, 'D']),
    0x8B: Opc('RES 1,E', 8, 2, sb.res_nr, [1, 'E']),
    0x8C: Opc('RES 1,H', 8, 2, sb.res_nr, [1, 'H']),
    0x8D: Opc('RES 1,L', 8, 2, sb.res_nr, [1, 'L']),
    0x8E: Opc('RES 1,(HL)', 16, 2, sb.res_nhl, [1]),
    0x8F: Opc('RES 1,A', 8, 2, sb.res_nr, [1, 'A']),
    0x90: Opc('RES 2,B', 8, 2, sb.res_nr, [2, 'B']),
    0x91: Opc('RES 2,C', 8, 2, sb.res_nr, [2, 'C']),
    0x92: Opc('RES 2,D', 8, 2, sb.res_nr, [2, 'D']),
    0x93: Opc('RES 2,E', 8, 2, sb.res_nr, [2, 'E']),
    0x94: Opc('RES 2,H', 8, 2, sb.res_nr, [2, 'H']),
    0x95: Opc('RES 2,L', 8, 2, sb.res_nr, [2, 'L']),
    0x96: Opc('RES 2,(HL)', 16, 2, sb.res_nhl, [2]),
    0x97: Opc('RES 2,A', 8, 2, sb.res_nr, [2, 'A']),
    0x98: Opc('RES 3,B', 8, 2, sb.res_nr, [3, 'B']),
    0x99: Opc('RES 3,C', 8, 2, sb.res_nr, [3, 'C']),
    0x9A: Opc('RES 3,D', 8, 2, sb.res_nr, [3, 'D']),
    0x9B: Opc('RES 3,E', 8, 2, sb.res_nr, [3, 'E']),
    0x9C: Opc('RES 3,H', 8, 2, sb.res_nr, [3, 'H']),
    0x9D: Opc('RES 3,L', 8, 2, sb.res_nr, [3, 'L']),
    0x9E: Opc('RES 3,(HL)', 16, 2, sb.res_nhl, [3]),
    0x9F: Opc('RES 3,A', 8, 2, sb.res_nr, [3, 'A']),
    0xA0: Opc('RES 4,B', 8, 2, sb.res_nr, [4, 'B']),
    0xA1: Opc('RES 4,C', 8, 2, sb.res_nr, [4, 'C']),
    0xA2: Opc('RES 4,D', 8, 2, sb.res_nr, [4, 'D']),
    0xA3: Opc('RES 4,E', 8, 2, sb.res_nr, [4, 'E']),
    0xA4: Opc('RES 4,H', 8, 2, sb.res_nr, [4, 'H']),
    0xA5: Opc('RES 4,L', 8, 2, sb.res_nr, [4, 'L']),
    0xA6: Opc('RES 4,(HL)', 16, 2, sb.res_nhl, [4]),
    0xA7: Opc('RES 4,A', 8, 2, sb.res_nr, [4, 'A']),
    0xA8: Opc('RES 5,B', 8, 2, sb.res_nr, [5, 'B']),
    0xA9: Opc('RES 5,C', 8, 2, sb.res_nr, [5, 'C']),
    0xAA: Opc('RES 5,D', 8, 2, sb.res_nr, [5, 'D']),
    0xAB: Opc('RES 5,E', 8, 2, sb.res_nr, [5, 'E']),
    0xAC: Opc('RES 5,H', 8, 2, sb.res_nr, [5, 'H']),
    0xAD: Opc('RES 5,L', 8, 2, sb.res_nr, [5, 'L']),
    0xAE: Opc('RES 5,(HL)', 16, 2, sb.res_nhl, [5]),
    0xAF: Opc('RES 5,A', 8, 2, sb.res_nr, [5, 'A']),
    0xB0: Opc('RES 6,B', 8, 2, sb.res_nr, [6, 'B']),
    0xB1: Opc('RES 6,C', 8, 2, sb.res_nr, [6, 'C']),
    0xB2: Opc('RES 6,D', 8, 2, sb.res_nr, [6, 'D']),
    0xB3: Opc('RES 6,E', 8, 2, sb.res_nr, [6, 'E']),
    0xB4: Opc('RES 6,H', 8, 2, sb.res_nr, [6, 'H']),
    0xB5: Opc('RES 6,L', 8, 2, sb.res_nr, [6, 'L']),
    0xB6: Opc('RES 6,(HL)', 16, 2, sb.res_nhl, [6]),
    0xB7: Opc('RES 6,A', 8, 2, sb.res_nr, [6, 'A']),
    0xB8: Opc('RES 7,B', 8, 2, sb.res_nr, [7, 'B']),
    0xB9: Opc('RES 7,C', 8, 2, sb.res_nr, [7, 'C']),
    0xBA: Opc('RES 7,D', 8, 2, sb.res_nr, [7, 'D']),
    0xBB: Opc('RES 7,E', 8, 2, sb.res_nr, [7, 'E']),
    0xBC: Opc('RES 7,H', 8, 2, sb.res_nr, [7, 'H']),
    0xBD: Opc('RES 7,L', 8, 2, sb.res_nr, [7, 'L']),
    0xBE: Opc('RES 7,(HL)', 16, 2, sb.res_nhl, [7]),
    0xBF: Opc('RES 7,A', 8, 2, sb.res_nr, [7, 'A']),
    0xC0: Opc('SET 0,B', 8, 2, sb.set_nr, [0, 'B']),
    0xC1: Opc('SET 0,C', 8, 2, sb.set_nr, [0, 'C']),
    0xC2: Opc('SET 0,D', 8, 2, sb.set_nr, [0, 'D']),
    0xC3: Opc('SET 0,E', 8, 2, sb.set_nr, [0, 'E']),
    0xC4: Opc('SET 0,H', 8, 2, sb.set_nr, [0, 'H']),
    0xC5: Opc('SET 0,L', 8, 2, sb.set_nr, [0, 'L']),
    0xC6: Opc('SET 0,(HL)', 16, 2, sb.set_nhl, [0]),
    0xC7: Opc('SET 0,A', 8, 2, sb.set_nr, [0, 'A']),
    0xC8: Opc('SET 1,B', 8, 2, sb.set_nr, [1, 'B']),
    0xC9: Opc('SET 1,C', 8, 2, sb.set_nr, [1, 'C']),
    0xCA: Opc('SET 1,D', 8, 2, sb.set_nr, [1, 'D']),
    0xCB: Opc('SET 1,E', 8, 2, sb.set_nr, [1, 'E']),
    0xCC: Opc('SET 1,H', 8, 2, sb.set_nr, [1, 'H']),
    0xCD: Opc('SET 1,L', 8, 2, sb.set_nr, [1, 'L']),
    0xCE: Opc('SET 1,(HL)', 16, 2, sb.set_nhl, [1]),
    0xCF: Opc('SET 1,A', 8, 2, sb.set_nr, [1, 'A']),
    0xD0: Opc('SET 2,B', 8, 2, sb.set_nr, [2, 'B']),
    0xD1: Opc('SET 2,C', 8, 2, sb.set_nr, [2, 'C']),
    0xD2: Opc('SET 2,D', 8, 2, sb.set_nr, [2, 'D']),
    0xD3: Opc('SET 2,E', 8, 2, sb.set_nr, [2, 'E']),
    0xD4: Opc('SET 2,H', 8, 2, sb.set_nr, [2, 'H']),
    0xD5: Opc('SET 2,L', 8, 2, sb.set_nr, [2, 'L']),
    0xD6: Opc('SET 2,(HL)', 16, 2, sb.set_nhl, [2]),
    0xD7: Opc('SET 2,A', 8, 2, sb.set_nr, [2, 'A']),
    0xD8: Opc('SET 3,B', 8, 2, sb.set_nr, [3, 'B']),
    0xD9: Opc('SET 3,C', 8, 2, sb.set_nr, [3, 'C']),
    0xDA: Opc('SET 3,D', 8, 2, sb.set_nr, [3, 'D']),
    0xDB: Opc('SET 3,E', 8, 2, sb.set_nr, [3, 'E']),
    0xDC: Opc('SET 3,H', 8, 2, sb.set_nr, [3, 'H']),
    0xDD: Opc('SET 3,L', 8, 2, sb.set_nr, [3, 'L']),
    0xDE: Opc('SET 3,(HL)', 16, 2, sb.set_nhl, [3]),
    0xDF: Opc('SET 3,A', 8, 2, sb.set_nr, [3, 'A']),
    0xE0: Opc('SET 4,B', 8, 2, sb.set_nr, [4, 'B']),
    0xE1: Opc('SET 4,C', 8, 2, sb.set_nr, [4, 'C']),
    0xE2: Opc('SET 4,D', 8, 2, sb.set_nr, [4, 'D']),
    0xE3: Opc('SET 4,E', 8, 2, sb.set_nr, [4, 'E']),
    0xE4: Opc('SET 4,H', 8, 2, sb.set_nr, [4, 'H']),
    0xE5: Opc('SET 4,L', 8, 2, sb.set_nr, [4, 'L']),
    0xE6: Opc('SET 4,(HL)', 16, 2, sb.set_nhl, [4]),
    0xE7: Opc('SET 4,A', 8, 2, sb.set_nr, [4, 'A']),
    0xE8: Opc('SET 5,B', 8, 2, sb.set_nr, [5, 'B']),
    0xE9: Opc('SET 5,C', 8, 2, sb.set_nr, [5, 'C']),
    0xEA: Opc('SET 5,D', 8, 2, sb.set_nr, [5, 'D']),
    0xEB: Opc('SET 5,E', 8, 2, sb.set_nr, [5, 'E']),
    0xEC: Opc('SET 5,H', 8, 2, sb.set_nr, [5, 'H']),
    0xED: Opc('SET 5,L', 8, 2, sb.set_nr, [5, 'L']),
    0xEE: Opc('SET 5,(HL)', 16, 2, sb.set_nhl, [5]),
    0xEF: Opc('SET 5,A', 8, 2, sb.set_nr, [5, 'A']),
    0xF0: Opc('SET 6,B', 8, 2, sb.set_nr, [6, 'B']),
    0xF1: Opc('SET 6,C', 8, 2, sb.set_nr, [6, 'C']),
    0xF2: Opc('SET 6,D', 8, 2, sb.set_nr, [6, 'D']),
    0xF3: Opc('SET 6,E', 8, 2, sb.set_nr, [6, 'E']),
    0xF4: Opc('SET 6,H', 8, 2, sb.set_nr, [6, 'H']),
    0xF5: Opc('SET 6,L', 8, 2, sb.set_nr, [6, 'L']),
    0xF6: Opc('SET 6,(HL)', 16, 2, sb.set_nhl, [6]),
    0xF7: Opc('SET 6,A', 8, 2, sb.set_nr, [6, 'A']),
    0xF8: Opc('SET 7,B', 8, 2, sb.set_nr, [7, 'B']),
    0xF9: Opc('SET 7,C', 8, 2, sb.set_nr, [7, 'C']),
    0xFA: Opc('SET 7,D', 8, 2, sb.set_nr, [7, 'D']),
    0xFB: Opc('SET 7,E', 8, 2, sb.set_nr, [7, 'E']),
    0xFC: Opc('SET 7,H', 8, 2, sb.set_nr, [7, 'H']),
    0xFD: Opc('SET 7,L', 8, 2, sb.set_nr, [7, 'L']),
    0xFE: Opc('SET 7,(HL)', 16, 2, sb.set_nhl, [7]),
    0xFF: Opc('SET 7,A', 8, 2, sb.set_nr, [7, 'A'])
}