import datetime as dt
import os
import requests
import time
import logging
import asyncio


logging.basicConfig(format='%(asctime)s %(message)s')
log = logging.getLogger()
log.setLevel(logging.INFO)


API_HISTORICAL = 'https://openexchangerates.org/api/historical/{}.json'
APP_ID = os.environ.get('APP_ID', 'b46b42a263f74e56938c537249adb198')
PERIOD_DAYS = int(os.environ.get('PERIOD', 10))

print(APP_ID)

"""
Как только перед функцией появляется async, функция становится корутиной
Нельзя использовать сигхронные библиотеки в асинхронной функции
socket - соединение 
асинхронная библиотека - та, которая умеет рабоать асинхроно с веб-соединениями

"""


async def get_rates():
    rates = []
    start_time = time.monotonic()
    today = dt.datetime.today()
    for days in range(PERIOD_DAYS):
        date = today - dt.timedelta(days=days)
        log.info('Starting API request for %s', date)

        response = requests.get(
            API_HISTORICAL.format(date.strftime('%Y-%m-%d')),
            params=dict(app_id=APP_ID)
        )

        if response.status_code == 200:
            log.info('Response received from %s', response.url)
            rates.append(response.content)
        else:
            log.error('Bad %s, status %d', response.url, response.status_code)

    log.info('Downloaded in %d ms', (time.monotonic() - start_time) * 1000)
    return rates


if __name__ == '__main__':
    asyncio.run(get_rates())
