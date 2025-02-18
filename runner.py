async def take_use_inp1():
    i1 = int(input('Enter is input 1: '))
    print('Input taken: ', i1)

async def take_use_inp2():
    i2 = int(input('Enter is input 2: '))
    print('Input taken: ', i2)

def sayHello(als, s):
    # print('Hello I am ',s)
    for i in range(50000000):
        als.append(f'Hello I am {s}')
    # with open('greet.txt', 'a') as f:
    #     for i in range(50000000):
    #         f.write(f'Hello I am {s}\n')


async def runner():
    # WARNING: It is going to consume lots of memory
    alst = []
    sayHello(alst, 'Yashu')
    task1 = asyncio.create_task(take_use_inp1())
    sayHello(alst, 'Thor')
    breakpoint()
    task2 = asyncio.create_task(take_use_inp2())
    sayHello(alst, 'Ironman')

import time
import asyncio

async def d1(t):
    for i in range(0, 10000000 * t):
        b = i * 3
        pass

async def d2(t):
    for i in range(0, 10000000 * t):
        b = i * 3
        pass

async def makeCoffe():
    print('Started making coffe.')
    # await asyncio.sleep(5)
    await asyncio.create_task(d1(10))
    print('Coffe is ready!')

async def toastBread():
    print('Started toasting bread.')
    # await asyncio.sleep(3)
    await asyncio.create_task(d2(3))
    print('Bread is ready!')

async def myFun():
    print('Start.....')
    time.sleep(5)
    print('End.......')

async def torun():
    print('Run it......')
    # await myFun()
    task = asyncio.create_task(myFun())
    print('Closed......')

async def main():
    start_time = time.time()
    batch = asyncio.gather(makeCoffe(), toastBread())
    await batch
    end_time = time.time()

    print('Total time: ', round(end_time - start_time))

# asyncio.run(main())

# asyncio.run(myFun())

# asyncio.run(torun())

asyncio.run(runner())