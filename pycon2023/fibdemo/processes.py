from concurrent.futures import ProcessPoolExecutor as Pool
from threading import Thread

from . import fib, req_handler, server


pool = Pool(4)


def handle_conn(client):
    run_fib = (lambda n: pool.submit(fib, n).result())
    Thread(target=req_handler, args=(client, run_fib), daemon=True).start()


if __name__ == '__main__':
    server(handle_conn)
