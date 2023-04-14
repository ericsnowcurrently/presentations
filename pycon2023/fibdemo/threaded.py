from . import fib, req_handler, server


if __name__ == '__main__':
    server(req_handler, fib)
