from threading import Thread

from . import fib, req_handler, server


def handle_conn(client):
    run_fib = fib
    Thread(target=req_handler, args=(client, run_fib), daemon=True).start()


if __name__ == '__main__':
    server(handle_conn)
