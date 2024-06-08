import asyncio
from datetime import datetime


async def task_1():
    """Bu yirda biz asyncion dasturlash tilidagi kod orqali funksiyaga timi sleep beramiz"""
    print(datetime.now())
    await asyncio.sleep(2)
    print("Task_1")
    print(datetime.now())


async def task_2():
    print(datetime.now())
    await asyncio.sleep(3)
    print("Task_2")
    print(datetime.now())


async def task_3():
    print(datetime.now())
    await asyncio.sleep(4)
    print("Task_3")
    print(datetime.now())


async def task_4():
    print(datetime.now())
    await asyncio.sleep(5)
    print("Task_4")
    print(datetime.now())


async def task_5():
    print(datetime.now())
    await asyncio.sleep(6)
    print("Task_5")
    print(datetime.now())


async def task_6():
    print(datetime.now())
    await asyncio.sleep(5)
    print("Task_6")
    print(datetime.now())


async def task_7():
    print(datetime.now())
    await asyncio.sleep(6)
    print("Task_7")
    print(datetime.now())


async def task_8():
    print(datetime.now())
    await asyncio.sleep(2)
    print("Task_8")
    print(datetime.now())


async def task_9():
    print(datetime.now())
    await asyncio.sleep(5)
    print("Task_9")
    print(datetime.now())


async def task_10():
    """Bu yirda biz barcha funksiyani birdaniga ishlatamiz va qaysi biri birinchi bo'lib bajarilishini ko'ramiz"""
    print(datetime.now())
    await asyncio.gather(task_1(), task_2(), task_3(), task_4(), task_5())
    print(datetime.now())


async def task_11():
    """Bu yirda biz barcha funksiyani birdaniga ishlatamiz va qaysi biri birinchi bo'lib bajarilishini ko'ramiz"""
    print(datetime.now())
    await asyncio.gather(task_6(), task_7(), task_8(), task_9())
    print(datetime.now())


async def task_12():
    """Bu yirda biz task_10 va task_11 larni farqini ko'rishimiz mumkun"""
    print(datetime.now())
    await asyncio.gather(task_10(), task_11())
    print(datetime.now())


if __name__ == '__main__':
    asyncio.run(task_10())
