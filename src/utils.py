# AUXILIARY
# TODO: optimize flag getter
def lbin_to_hex(list_):
    # Rename, we just use the number, hex is not necesary
    string = ''.join([str(x) for x in list_])
    numb = int(string, 2)
    return numb


def hex_to_lbin(hex_):
    bin_ = bin(hex_)[2:].zfill(8)
    list_ = [int(x) for x in bin_]
    return list_
