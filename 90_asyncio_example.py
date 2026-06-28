# Asyncio Example
import asyncio

async def fetch_data(id, delay):
    print(f"Task {id}: Starting fetch...")
    await asyncio.sleep(delay)
    print(f"Task {id}: Finished fetch after {delay} seconds")
    return {"id": id, "data": "sample data"}

async def main():
    print("Starting main routine")
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3)
    )
    print("All tasks finished:", results)

if __name__ == "__main__":
    asyncio.run(main())
