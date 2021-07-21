import asyncio
import aiohttp
from Threading import blog_spider


# 单线程异步爬虫（协程），没有线程切换，快于多线程
# 信号量，控制一定的并发数量10个
semaphore = asyncio.Semaphore(10)

async def async_craw(url):
    async with semaphore:
        print("craw url:", url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                print(f"craw url:{url}, {len(result)}")


loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls
]

import time

start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("use time secons:", end - start)