import aiohttp
import asyncio
from bs4 import BeautifulSoup
import requests

url = 'https://fashionunited.ru/novostee/moda'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


async def main():
    w = open('articles.txt', 'w')
    w.close()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                bs = BeautifulSoup(html, 'html.parser')
                h2_elements = bs.find_all('h2')
                p_elements = bs.find_all('p')

                for h2, p in zip(h2_elements, p_elements):
                    if (h2.text != "loading..." and p.text != "loading..."):
                        w = open('articles.txt', 'a')
                        w.write('{\n')
                        w.write(f'{h2.text}\n')
                        w.write('\n')
                        w.write(f'{p.text}\n')
                        w.write('}\n\n')
                        w.close()

            else:
                print(f"Error fetching content. Status code: {response.status}")

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
except requests.RequestException as e:
    print(f"Error fetching content: {e}")
