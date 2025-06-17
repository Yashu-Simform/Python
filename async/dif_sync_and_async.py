import time
import asyncio

async def mytimer():
    for i in range(1000):
        time.sleep(2)
        print(i)

def get_data_from_db():
    print('Initializing to retrive data ...')
    
    asyncio.run(mytimer())

    for i in range(1000, 2000):
        print('----', i)
    print('Data retrived successfully!')

async def async_get_data_from_db():
    print('Initializing to retrive data ... asynchronously')
    await mytimer()
    
    for i in range(1000, 2000):
        print('----', i)
    print('Data retrived successfully!  asynchronously')

if __name__ == "__main__":
    get_data_from_db()
    # asyncio.run(async_get_data_from_db())