from threading import Thread
from threading import Lock

count = 0

lock = Lock()


def increase():
    global count
    with lock:
        count += 1
        print(count)


def decrease():
    global count
    with lock:
        count -= 1
        print(count)


tasks = []


def do_increase_decrease(x: int):
    for _ in range(x):
        tasks.append(Thread(target=increase, args=()))
        tasks.append(Thread(target=decrease, args=()))

    for task in tasks:
        task.start()


if __name__ == "__main__":
    do_increase_decrease(40)
