# from https://www.youtube.com/watch?v=MCs5OvhV9S4
# https://github.com/dabeaz/concurrencylive

# export PYTHONWARNINGS=ignore

from socket import *
from threading import Thread
import time


PATH_ENTRY = __file__.rpartition('/')[0].rpartition('/')[0]

address = ('', 25000)


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def req_handler(client, run_fib):
    while True:
        try:
            req = client.recv(100)
        except ConnectionResetError:
            req = b''
        if not req:
            break
        n = int(req)

        result = run_fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    client.close()
    print("Closed")


def server(handle_conn, run_fib):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        t = Thread(
            target=handle_conn,
            args=(client, run_fib),
            daemon=True,
        ).start()


def client_show_long_running():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 25000))

    try:
        while True:
            start = time.time()
            sock.send(b'30')
            resp =sock.recv(100)
            end = time.time()
            print(end-start)
    except (KeyboardInterrupt, ConnectionResetError):
        pass
    sock.close()


def client_show_rate():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 25000))

    n = 0

    done = False
    def monitor():
        nonlocal done
        try:
            nonlocal n
            while not done:
                time.sleep(1)
                print(n, 'reqs/sec')
                n = 0
        except (KeyboardInterrupt, ConnectionResetError):
            done = True
    from threading import Thread
    Thread(target=monitor).start()

    try:
        while not done:
            sock.send(b'1')
            resp =sock.recv(100)
            n += 1
    except (KeyboardInterrupt, ConnectionResetError):
        done = True
    sock.close()
