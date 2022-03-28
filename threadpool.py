from concurrent.futures import ThreadPoolExecutor
import time


def sleep_x_seconds(x):
    time.sleep(x)
    print("Guten morgen :))")


executor = ThreadPoolExecutor(max_workers=10)

print("Program start")
future_list = {executor.submit(sleep_x_seconds, 1): i for i in range(10)}
print("Program end")
