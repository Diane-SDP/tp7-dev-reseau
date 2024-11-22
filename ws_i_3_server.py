import asyncio
import websockets

global CLIENTS
CLIENTS = []


async def handle_client_msg(websocket):
    pseudo = await websocket.recv()
    CLIENTS.append([pseudo, websocket])
    print(f"nouveau client : {pseudo}")
    try:
        while True:
            msg = await websocket.recv()
            disconnected = []
            for client in CLIENTS:
                try:
                    await client[1].send(f"{pseudo} :  {msg}")
                except websockets.exceptions.ConnectionClosed:
                    disconnected.append(client)
            for client in disconnected:
                CLIENTS.remove(client)
    except websockets.exceptions.ConnectionClosed:
        print("Client déconnecté")
        CLIENTS.remove([pseudo, websocket])



async def main():
    async with websockets.serve(handle_client_msg, "localhost", 8765):
        await asyncio.Future()
    
if __name__ == "__main__":
    asyncio.run(main())