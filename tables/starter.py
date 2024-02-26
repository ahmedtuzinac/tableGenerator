import asyncio
from table import *

if __name__ == '__main__':
    import time

    start_time = time.time()
    asyncio.run(create_table())
    end_time = time.time()
    print(f'Duration of executing script: {round(end_time - start_time, 3)} seconds.')

    with open('executionTimeHistory.txt', 'a') as file:
        file.write(f'Duration of executing script: {round(end_time - start_time, 5)} seconds.\n')
