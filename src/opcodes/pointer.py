from .meta import pointer, cb_pointer, Opc


def fetch_opc_info(cpu, opc) -> Opc:
    # TODO: Control CB header
    return pointer[opc]
