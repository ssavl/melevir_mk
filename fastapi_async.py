import asyncio
import datetime as dt
import os
import requests
import time
import logging
import random
import httpx
import fastapi


logging.basicConfig(format='%(asctime)s %(message)s')
log = logging.getLogger()
log.setLevel(logging.INFO)

api = fastapi.FastAPI()


API_HISTORICAL = 'https://openexchangerates.org/api/historical/{}.json'
APP_ID = os.environ.get('APP_ID', 'b46b42a263f74e56938c537249adb198')
PERIOD_DAYS = int(os.environ.get('PERIOD', 2))


async def get_rates_for(client, date):
    log.info('Starting API request for %s', date)
    content = None

    if random.choice([True, False]):
        raise BaseException


    response = await client.get(
        API_HISTORICAL.format(date.strftime('%Y-%m-%d')),
        params=dict(app_id=APP_ID)
    )

    if response.status_code == 200:
        log.info('Response received from %s', response.url)
        content = response.json()
    else:
        log.error('Bad %s, status %d', response.url, response.status_code)

    return rates


async def get_rates(period_days):
    rates = []
    tasks = []
    start_time = time.monotonic()
    today = dt.datetime.today()
    async with httpx.AsyncClient() as client:
        for days in range(period_days):
            date = today - dt.timedelta(days=days)
            tasks.append(asyncio.create_task(get_rates_for(client, date)))
        try:
            rates = await asyncio.gather(*tasks)
        except BaseException:
            log.error('error')
            for task in tasks:
                if task.done():
                    if task.exception() is None:
                        rates.append(task.result())
                        log.info('task %s done', task.get_name())
                    else:
                        log.info('task %s has exception', task.get_name())
                else:
                    task.cancel()
                    log.info('task %s not done', task.get_name())

    cancelled = filter(lambda t: not t.done(), tasks)
    while list(cancelled):
        await asyncio.sleep(0.1)
        cancelled = filter(lambda t: not t.done(), tasks)
    for task in tasks:
        log.info('Task %s state cancelled=%s', task.get_name(), task.cancel())


    log.info('Downloaded in %d ms', (time.monotonic() - start_time) * 1000)
    return rates


@api.get('/rates/')
async def rates(period_days: int = 1, currency: str = 'RUB'):
    rates = await get_rates(period_days)

    return {'rates': [dict(date=r['timestamp'], currency=r['rates'][currency]) for r in rates]}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(api, host="0.0.0.0", port=8000)
