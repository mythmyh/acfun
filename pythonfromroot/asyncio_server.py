
import asyncio
import datetime
import random
import websockets
from ontime2 import single2


async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        name = await websocket.recv()
        print(name.startswith('https'))
        if 'https://www.acfun.cn' in name:
            single2(name)

        #await websocket.send(now)
        #await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "192.168.1.72", 8766)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
