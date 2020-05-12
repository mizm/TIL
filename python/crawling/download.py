import asyncio
import aiohttp

async def download(i: int):
    index = f'{i:02d}'
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://www28.atpages.jp/petitindex/SAO4_{index}.txt') as res:
            with open(f'{index}.txt', 'w') as f:
                f.write(await res.text())


tasks = [download(x) for x in range(1, 59+1)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))