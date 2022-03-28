import sys
import hashlib
from threading import Thread


def create_encoded_n(n):
    multp = 1024 * 1024 * 1024
    ambstr = "a" * multp
    string = ambstr.encode()
    for i in range(n):
        yield string[i: int((i+1) * multp / n - 1)]


def threaded_hashing(n):
    lst = list(create_encoded_n(n))
    for i in range(n):
        t = Thread(target=hashlib.sha256, args=(lst[i],))
        t.start()


def no_threading(n):
    lst = list(create_encoded_n(n))
    for i in range(n):
        hashlib.sha256(lst[i])


if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    if arg1 == 'threaded':
        threaded_hashing(int(arg2))
    else:
        no_threading(int(arg2))
