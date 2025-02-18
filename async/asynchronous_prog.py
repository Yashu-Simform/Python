import asyncio, time

async def take_userinput():
    a = int(input('Enter value of a: '))
    b = int(input('Enter value of b: '))

    return (a,b)

async def multiply(vals):
    await asyncio.sleep(3)
    a, b = vals
    ans = a * b
    print('Multiplication completed! \nAns: ', ans)
    # return ans

async def add(vals):
    await asyncio.sleep(1)
    a, b = vals
    ans = a + b
    print('Addition Completed! \nAns: ', ans)
    # return ans

async def divide(vals):
    await asyncio.sleep(3)
    a, b = vals
    ans = a // b
    print('Division completed! \nAns: ', ans)
    # return ans

async def substract(vals):
    await asyncio.sleep(1)
    a, b = vals
    ans = a - b
    print('Substraction Completed! \nAns: ', ans)
    # return ans

async def batch1(vals):
    task1 = asyncio.create_task(multiply(vals))
    task2 = asyncio.create_task(add(vals))
    await task1
    await task2

async def batch2(vals):
    batch = asyncio.gather(divide(vals), substract(vals))
    await batch


async def waiter(task):
    while task.done:
        pass

async def handler():
    print('Tasks started')
    vals = await take_userinput()
    batch = asyncio.gather(batch1(vals), batch2(vals))
    await batch
    
    print('All task done!')


asyncio.run(handler())