import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        msg = input("What's your message? ")
        await websocket.send(msg)
        response = await websocket.recv()
        print(f"{response}")

if __name__ == "__main__":
    asyncio.run(hello())
