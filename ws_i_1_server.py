import asyncio
import websockets

async def hello(websocket):
    msg = await websocket.recv()
    print(msg)
    response = f"Hello client ! Received \"{msg}\""
    await websocket.send(response)


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())
