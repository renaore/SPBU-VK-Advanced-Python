import os
import aiohttp
import asyncio
import aiofiles

async def download_image(session, url, file_path):
    async with session.get(url) as resp:
        if resp.status == 200:
            async with aiofiles.open(file_path, mode='wb') as f:
                await f.write(await resp.read())
async def main():
    folder_path = '../artifacts/5_1/images'
    os.makedirs(folder_path, exist_ok=True )

    number_of_images = int(input('Введите число скачиваемых картинок: '))
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(number_of_images):
            url = f"https://picsum.photos/1024/1024?random={i}"
            file_path = os.path.join(folder_path, f'image_{i + 1}.jpg')
            tasks.append(download_image(session, url, file_path))
        await asyncio.gather(*tasks)

asyncio.run(main())