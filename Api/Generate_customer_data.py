import random
import time
import asyncio
import aiohttp

def generate_name():
    first_name = random.choice(["John", "Mary", "Peter", "Jane", "David", "Elizabeth", "Michael", "Susan", "Christopher", "Jennifer"])
    last_name = random.choice(["Smith", "Jones", "Williams", "Brown", "Davis", "Wilson", "Taylor", "Thompson", "White", "Green"])
    full_name = f"{first_name} {last_name}"
    email = f"{full_name.replace(' ', '.').lower()}{random.randint(1,30)}@example.com"
    username = full_name.replace(' ', '').lower()
    return full_name, email, username

async def send_post_request(session, data):
    url = 'http://localhost:5000/api/customers'
    try:
        async with session.post(url, json=data) as response:
            return await response.json()
    except aiohttp.ClientError as e:
        print("Error:", e)

async def main():
    start_time = time.time()

    num_requests = 50  # Number of individual POST requests to be sent

    names_emails_usernames = [generate_name() for _ in range(num_requests)]

    async with aiohttp.ClientSession() as session:
        tasks = [send_post_request(session, {"name": name, "email": email, "username": username}) for name, email, username in names_emails_usernames]
        results = await asyncio.gather(*tasks)

    end_time = time.time()

    print(f"Time taken to send {num_requests} POST requests: {end_time - start_time:.6f} seconds")
    print("Responses:", results)

if __name__ == "__main__":
    asyncio.run(main())
