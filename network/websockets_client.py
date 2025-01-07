#!/usr/bin/env python
import time

"""Client using the asyncio API."""

import asyncio
from websockets.asyncio.client import connect


async def hello():
    async with connect("ws://localhost:8765") as websocket:
        message = "Hello, world!"
        print(f"Connected to {websocket.remote_address}")
        while True:
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received: {response}")
            time.sleep(1)


if __name__ == "__main__":
    asyncio.run(hello())