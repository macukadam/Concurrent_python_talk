# import requests as r
from threading import Thread
import time


def sleep_and_print(wait: int):
    time.sleep(wait)
    print("Woow much a long sleep")


t = []


def you_need_to_wait_for_server_to_respond_x_times(x: int):
    for _ in range(x):
        t = Thread(target=sleep_and_print, args=(1,))
        t.start()


if __name__ == '__main__':
    print("Program start")
    you_need_to_wait_for_server_to_respond_x_times(5)
    print("Program end")
