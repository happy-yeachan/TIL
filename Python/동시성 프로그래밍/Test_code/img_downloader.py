import os
import aiohttp
import asyncio
import aiofiles
from secrets import userid, userpass

# pip install aiofiles==0.7.0


async def img_downloader(session, img):
    img_name = img.split("/")[-1].split("?")[0]

    try:
        os.mkdir("Python/동시성 프로그래밍/Test_code/images")
    except FileExistsError:
        pass

    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"Python/동시성 프로그래밍/Test_code/images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)


async def fetch(session, url, i):
    print(i + 1)
    headers = {
        "X-Naver-Client-Id": id,
        "X-Naver-Client-Secret": pas,
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        print(result)
        items = result["items"]
        images = [item["link"] for item in items]
        await asyncio.gather(*[img_downloader(session, img) for img in images])


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1+ i*20}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
