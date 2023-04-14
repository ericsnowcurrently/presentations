from test.support import interpreters
from threading import Thread

from . import PATH_ENTRY


def handle_in_new_interp(client, **kwargs):
    interp = interpreters.create(**kwargs)
    interp.run(f'''if True:
        from socket import socket
        import sys
        sys.path.insert(0, {PATH_ENTRY!r})
        from fibdemo import fib, req_handler
        client = socket(fileno={client.fileno()})
        req_handler(client, fib)
        ''')


def handle_conn_own_gil(client, run_fib):
    assert run_fib is None
    handle_in_new_interp(client, isolated=True)


def handle_conn_shared(client, run_fib):
    assert run_fib is None
    handle_in_new_interp(client, isolated=False)


if __name__ == '__main__':
    import sys
    from . import server
    HANDLERS = {
        '--isolated': handle_conn_own_gil,
        '--shared': handle_conn_shared,
    }
    try:
        handle_conn = HANDLERS[sys.argv[1]]
    except IndexError:
        handle_conn = handle_conn_own_gil
    server(handle_conn, None)
