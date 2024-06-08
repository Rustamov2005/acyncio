from datetime import datetime
import time


def task_1():
    """Bu yirda funksiyani 2 sekun kutib turib ishlashini taminlaganman time.sleep orqali"""
    print(datetime.now())
    time.sleep(2)
    print('Task 1')
    print(datetime.now())


def task_2():
    print(datetime.now())
    time.sleep(3)
    print('Task 2')
    print(datetime.now())


def task_3():
    print(datetime.now())
    time.sleep(4)
    print('Task 3')
    print(datetime.now())


def task_4():
    print(datetime.now())
    time.sleep(5)
    print('Task 4')
    print(datetime.now())


def task_5():
    print(datetime.now())
    time.sleep(6)
    print('Task 5')
    print(datetime.now())


def task_6():
    print(datetime.now())
    time.sleep(7)
    print('Task 6')
    print(datetime.now())


def task_7():
    print(datetime.now())
    time.sleep(8)
    print('Task 7')
    print(datetime.now())


def task_8():
    print(datetime.now())
    time.sleep(9)
    print('Task 8')
    print(datetime.now())


def task_9():
    print(datetime.now())
    time.sleep(10)
    print('Task 9')
    print(datetime.now())


def task_10():
    """Bu yirda manashu tasklarni bajarish uchun qancha vaqt ketganligini ko'rishimiz mumkun"""
    print(datetime.now())
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    print(datetime.now())


def task_11():
    """Bu yirda 4 ta funksiya uchun qancha vaqt ketganligini ko'rishimiz mumkun"""
    print(datetime.now())
    task_6()
    task_7()
    task_8()
    task_9()
    print(datetime.now())


def task_12():
    """Bu funksiya orqali biz task_10 va task_11 funksiyalarning umumiy vaqtlari farqini ko'rishimiz mumkun"""
    print(datetime.now())
    task_10()
    print(datetime.now())
    task_11()
    print(datetime.now())


if __name__ == '__main__':
    task_12()