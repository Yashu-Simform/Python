#Task to do asynchronously
#1. Calculate and print prime numbers within given range
#2. Calculate and print factorial of a number


import asyncio, time, math


def checkPrime(n, i, thresh):
    if i < thresh:
        return True
    
    if n%i == 0:
        return False
    
    return (True or checkPrime(n, i-1, thresh))

async def givePrime(n, i = 0):
    if i <= n:
        if checkPrime(n, n-1, math.floor(math.sqrt(i))):
            print('Prime num: ', i)

        await asyncio.sleep(2)
        await givePrime(n, i+1)


async def giveFactorial(n, thresh):
    if n == 0:
        return 1
    
    await asyncio.sleep(1)
    print('i = ', n)
    ans = n * (await giveFactorial(n-1, thresh))

    # print(ans)
    if n == thresh:
        print(ans)
    return ans

    # ans = 1
    # for i in range(1,n+1):
    #     ans = ans * i

    # return ans

# asyncio.run(givePrime(0, 5))

async def takeUserInputs():
    n = int(input('Enter a number: '))
    return n

async def main():
    n = await takeUserInputs()

    start_time = round(time.time())

    batch = asyncio.gather(givePrime(n), giveFactorial(n, n))
    fac = await batch

    print('Result: ', fac)

    # task1 = asyncio.create_task(giveFactorial(n))
    # await task1

    # print(f'Prime nums upto {n}: ', await givePrime(n))

    end_time = round(time.time())

    print('Total time taken: ', (end_time-start_time))

asyncio.run(main())