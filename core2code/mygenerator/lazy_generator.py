import os
import psutil
import time


# 现实当前python程序占用的内存大小
def show_momory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print(f"{hint} memory used:{memory}")


def test_iterator():
    show_momory_info("initing iterator")
    list_1 = [i for i in range(100000000)]
    show_momory_info("after iterator initiated")
    print(sum(list_1))
    show_momory_info("after sum called")


def test_generator():
    show_momory_info("initing generator")
    list_2 = (i for i in range(100000000))
    show_momory_info("after generator initiated")
    print(sum(list_2))
    show_momory_info("after sum called")

test_iterator()
test_generator()
