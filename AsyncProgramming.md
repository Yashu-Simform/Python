# Asynchronous Programming in Python

-   Async programming simply means to execute the functions concurrently or in an non-blocking manner.
-   ### Asynchronous Programming != Execution with multiple threads
-   ### Asynchronous programming = Execution within one thread only.

-   ## Firstly let's understand - How Synchronous Programming works ?
    -   In Synchronous programming there is one main thread allocated for the whole application. So when we run an application all the functions are executed using this main thread only. 
    -   Now the whole program is executed in some order, so when any function is called the main thread runs it by giving access to the resources(CPU, memory, etc.).
    -    So when any function takes longer time others need to wait to let main thread completes that function and gets free to run the next instruction. 
    -   Say there is func1() which takes input from user and store it in variable and after that there is other function func2() which just prints some message, have to wait for func1 to get executed first.
    -   In simple terms in synchronous programming each and every function gets executed in order they are called and after the previous functions execution gets completed. 
    -   Thus one functoin can block the main thread to further execute the program.

-   Now in Async programming we can avoid this blocking of one thread which is running the program.
-   ## Coroutines - Functions of Async programming
    -   In Async programming we declare the coroutines which can stop its executions in between adn can start from where it left off.
    -   Coroutines can be declared using `async` keyword.
    -   <b>Note</b>: When you call the async functions python interpreter interpretes as coroutine and returns a coroutine object.
    -   These coroutine objects have the execution context, function state, etc. with itself. 
        -   Example:
            ```
                async def connect_server():
                    # Connecting to server
                    connection = connect()
                    return connection
            ```
    -   Now these coroutines have different states as :
        -   CORO_CREATED - Not started yet
        -   CORO_RUNNING - Actively executing
        -   CORO_SUSPENDED - waiting for the result of `await` operation
        -   CORO_CLOSED - Finished execution

    -   As these coroutines can stop its execution in between and can starts where it left off, then where does the coroutines goes after stoping its execution in between ?. Ans. -> Event Loop
    -   After stoping its execution in between coroutine preserves the execution context of the async function and added to event loop.

-   Now we know how to create a coroutines, but to runt the coroutines we need to register or add it to event loop which manages its execution and scheduling.

-   ## What is Event Loop?
    -   An Event Loop is the core component of the python's async framework (asyncio).
    -   What does it do?
        -   Manages coroutine execution
        -   Handles I/O operation efficiently.
        -   Schedules tasks that uses async/await.

-   Thus any coroutine not scheduled in event loop will not going to run asynchronously.
-   Special: Any coroutine which are awaited inside any other coroutine will we added to event loop itself.

-   # How to schedule a coroutine to an event loop?
    -   There are 4 ways to schedule the coroutine to an event loop:
        -   `asyncio.run(coroutine())`: It schedules and run the coroutine into a new event loop.
        -   `asyncio.create_task(coroutine())`: It schedules the coroutine and run in background thus allowing main thread to execute further.
        -   `asyncio.gather(coroutine1(), coroutine2())`: Schedules multiple coroutines together
        -   `await coroutine()` : If used inside any other coroutine will schedule the awaited coroutine 

-   ## How to run async program?
    -   `asyncio.run(coroutine())` is used to run the async program, 
        -   It should be called only once to create the event loop.
        -   It cannot be called inside any active event loop if done so will throw an error.
        -   It BLOCKS the execution and wait until the whole async program gets executed.
        -   It terminates the event loop after the execution of the async program.
        
    -   `asyncio.create_task(coroutine())`: Is used to schedule the coroutine to an already active event loop.
        -   It just schedules the coroutine to an already active event loop.
        -   It does not block the execution but allow the main thread to execute rest of the program concurrently with the scheduled coroutine.
        -   Must be used inside a coroutine.

    -   Example:
        ```
            def get_brief_intro():
                intro()

            async def connect_to_db():
                connection = await connect()
                return connection

            async def main_coroutine():
                print('Welcome!')
                asyncio.create_task(connect_to_db())    <- Scheduled coroutine, going to run in background in non blocking manner

                get_brief_intro()  <- Normal function

            main_coroutine_obj = main_coroutine()
            asyncio.run(main_coroutine_obj) <- Entry point, starts async program
        ```