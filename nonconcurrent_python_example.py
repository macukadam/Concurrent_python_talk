import time


def sleep_for_x_seconds(x: int):
    time.sleep(x)
    print("Wow such a long sleep")


if __name__ == '__main__':
    print("Program start")
    sleep_for_x_seconds(1)
    print("Program end")
