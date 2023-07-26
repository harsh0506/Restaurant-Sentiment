import random
import time
from datetime import datetime, timedelta
import asyncio
import aiohttp


def generate_review():
    rating = random.randint(1, 5)
    food = random.choice(["pizza", "pasta", "burger", "salad",
                         "steak", "chicken", "fish", "dessert", "drink"])
    ambience = random.choice(["nice", "bland", "noisy", "crowded",
                             "romantic", "casual", "classy", "homey", "sterile"])
    hygiene = random.choice(["clean", "dirty", "well-maintained", "run-down",
                            "sanitary", "unsanitary", "disgusting", "spotless", "filthy"])
    service = random.choice(["excellent", "good", "bad", "terrible",
                            "slow", "fast", "friendly", "rude", "inattentive"])
    review = f"The {food} was delicious! The ambience was {ambience}, the hygiene was {hygiene}, and the service was {service}."
    # Generate random datetime between 1st January 2023 and 31st March 2023
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 3, 31)
    random_datetime = start_date + \
        timedelta(seconds=random.randint(
            0, int((end_date - start_date).total_seconds())))

    # Format the datetime as a SQL datetime string (e.g., "2023-01-20 12:34:56")
    postgres_datetime = random_datetime.strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "review": review,
        "food": random.randint(1, 5),
        "ambience": random.randint(1, 5),
        "hygiene": random.randint(1, 5),
        "service": random.randint(1, 5),
        "RId": random.randint(1, 5),
        "Cid": random.randint(12, 200),
        "Date": postgres_datetime,
    }

    return data


async def send_post_request(session, data):
    print(data)

    headers = {'Content-Type': 'application/json'}

    url = 'http://localhost:5000/api/reviews'
    try:
        async with session.post(url, headers=headers, json=data) as response:
            return await response.json()
    except aiohttp.ClientError as e:
        print("Error:", e)


async def main():
    start_time = time.time()

    num_requests = 100
    reviews = [generate_review() for _ in range(num_requests)]

    async with aiohttp.ClientSession() as session:
        tasks = [send_post_request(session, data) for data in reviews]
        results = await asyncio.gather(*tasks)

    end_time = time.time()

    print(
        f"Time taken to send {num_requests} POST requests: {end_time - start_time:.6f} seconds")
    print("Responses:", results)


if __name__ == "__main__":
    asyncio.run(main())
