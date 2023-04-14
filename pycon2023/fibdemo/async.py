import asyncio

from . import fib


async def handle_conn(reader, writer):
    """This is the async version of fibdemo.req_handler()."""
    while True:
        req = await reader.read(100)
        if not req:
            break
        n = int(req)
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        writer.write(resp)
        await writer.drain()


async def client_connected(reader, writer):
    addr = '???'
    print("connection", addr)
    await handle_conn(reader, writer)


async def main():
    server = await asyncio.start_server(client_connected, '127.0.0.1', 25000)
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
