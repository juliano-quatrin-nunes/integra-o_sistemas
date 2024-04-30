import asyncio
import websockets
import json

async def soma(websocket, path):
    data = await websocket.recv()
    
    resDict = json.loads(data)

    sum = float(resDict["input1"]) + float(resDict["input2"])

    await websocket.send(f"{sum}")

start_server = websockets.serve(soma, 'localhost', 8764)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()