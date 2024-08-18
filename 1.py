import requests
import time
import asyncio




def load_data_from_links(links):
    data = []
    for link in links:
        response = requests.get(link)
        data.append(response.text)
    return data

links = ['https://www.google.kz/1', 'https://www.google.kz/2', 'https://www.google.kz/3', 'https://www.google.kz/4','https://www.google.kz/5','https://www.google.kz/6','https://www.google.kz/7','https://www.google.kz/8','https://www.google.kz/9','https://www.google.kz/10',
         'https://www.google.kz/11','https://www.google.kz/12','https://www.google.kz/13','https://www.google.kz/14','https://www.google.kz/15','https://www.google.kz/16','https://www.google.kz/17','https://www.google.kz/18','https://www.google.kz/19','https://www.google.kz/20',
         'https://www.google.kz/21','https://www.google.kz/22','https://www.google.kz/23','https://www.google.kz/24','https://www.google.kz/24','https://www.google.kz/26','https://www.google.kz/27','https://www.google.kz/28','https://www.google.kz/29','https://www.google.kz/30',
         'https://www.google.kz/31','https://www.google.kz/32','https://www.google.kz/33','https://www.google.kz/34','https://www.google.kz/35','https://www.google.kz/36','https://www.google.kz/37','https://www.google.kz/38','https://www.google.kz/39','https://www.google.kz/40',
         'https://www.google.kz/41','https://www.google.kz/42','https://www.google.kz/43','https://www.google.kz/44','https://www.google.kz/45','https://www.google.kz/46','https://www.google.kz/47','https://www.google.kz/48','https://www.google.kz/49','https://www.google.kz/50',
         'https://www.google.kz/51','https://www.google.kz/52','https://www.google.kz/53','https://www.google.kz/54','https://www.google.kz/55','https://www.google.kz/56','https://www.google.kz/57','https://www.google.kz/58','https://www.google.kz/59','https://www.google.kz/60',
         'https://www.google.kz/61','https://www.google.kz/62','https://www.google.kz/63','https://www.google.kz/64','https://www.google.kz/65','https://www.google.kz/66','https://www.google.kz/67','https://www.google.kz/68','https://www.google.kz/69','https://www.google.kz/70',
         'https://www.google.kz/71','https://www.google.kz/72','https://www.google.kz/73','https://www.google.kz/74','https://www.google.kz/75','https://www.google.kz/76','https://www.google.kz/77','https://www.google.kz/78','https://www.google.kz/79','https://www.google.kz/80',
         'https://www.google.kz/81','https://www.google.kz/82','https://www.google.kz/83','https://www.google.kz/84','https://www.google.kz/85','https://www.google.kz/86','https://www.google.kz/87','https://www.google.kz/88','https://www.google.kz/89','https://www.google.kz/90',
         'https://www.google.kz/91','https://www.google.kz/92','https://www.google.kz/93','https://www.google.kz/94','https://www.google.kz/95','https://www.google.kz/96','https://www.google.kz/97','https://www.google.kz/98','https://www.google.kz/99','https://www.google.kz/100']




start_time = time.time()
data = load_data_from_links(links)
end_time = time.time()
print(f"Время выполнения: {end_time - start_time} секунд")





async def fetch_data(link):
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, link)
    return response.text

async def load_data_async(links):
    tasks = [fetch_data(link) for link in links]
    return await asyncio.gather(*tasks)



start_time = time.time()
data = asyncio.run(load_data_async(links))
end_time = time.time()
print(f"Время выполнения (асинхронно): {end_time - start_time} секунд")

