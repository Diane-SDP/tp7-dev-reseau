import asyncio
import redis.asyncio as redis 
import websockets
import uuid

global db
db = redis.Redis(host="10.1.1.254", port=6379)

async def handle_client_msg(websocket):
    pseudo = await websocket.recv()
    user_uuid = str(uuid.uuid4())
    await addclient(user_uuid, pseudo)
    await websocket.send(f"UUID:{user_uuid}")
    # CLIENTS.append([pseudo, websocket])
    print(f"nouveau client : {pseudo}")
    try:
        while True:
            data = await websocket.recv()
            uuid = data.split("|")[0]
            msg = data.split("|")[1]
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

async def addclient(uuid, pseudo) : 
    await db.set(uuid, [pseudo, True])

    
if __name__ == "__main__":
    asyncio.run(main())
