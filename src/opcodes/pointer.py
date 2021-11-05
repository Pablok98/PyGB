from .meta import pointer, cb_pointer, Opc


def fetch_opc_info(cpu, opc, cb=False) -> Opc:
    if not cb:
        return pointer[opc]
    else:
        return cb_pointer[opc]
