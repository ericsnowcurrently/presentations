from concurrent.futures import ProcessPoolExecutor as Pool

from . import fib, req_handler, server


pool = Pool(4)


def run_fib(n):
    future = pool.submit(fib, n)
    return future.result()


if __name__ == '__main__':
    server(req_handler, run_fib)
