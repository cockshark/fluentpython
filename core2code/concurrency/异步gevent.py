"""
gevent提供了两种机制来使能异步编程
   1.  对标准的I/O函数做了猴子补丁， 把他们变成了异步， 并且它也有一个greenlet对象能被用于并发执行
        greenlet是一种携程， 能够被想象成显成，所有的greenlet在同一物理线程上运行
        也就是说， gevent的调度器在IO等待期间使用同一个事件循环在所有的greenlets间来回切换， 而不是使用多个CPU来运行他们
    2. Future 由gevent.spawn来创建， 使用了一个函数和传递给这个函数的参数，并且启动了一个负责运行这个函数的greenlet。
        greenlet能够被看作一个future， 因为你声明的函数一旦运行完成，它的值就会包含在greenlet的value域中
"""

from gevent import monkey

monkey.patch_socket()

import gevent
from gevent.lock import Semaphore
import urllib.request as req
import string
import random


def gen_urls(base_urls, num_urls):
    for i in range(num_urls):
        yield base_urls + "".join(random.sample(string.ascii_lowercase, 10))


def chunked_requests(urls, chunk_size=100):
    semaphore = Semaphore(chunk_size)
    # 这里生成了一个信号量来让chunk_size下载发生
    requests = [gevent.spawn(download, u, semaphore) for u in urls]
    # 通过信号量用作一个上下文管理器， 我们确保了只有chunk_size数量的greenlet能够在同一时刻运行上下文主体部分
    for response in gevent.iwait(requests):
        yield response


def download(url, semaphore):
    with semaphore:
        # 我们能够把所需数量的greenlets放在队列中， 知道他们之中没有一个会运行直到我们用wait或者iwait启动一个事件循环
        data = req.urlopen(url)
        return data.read()


def run_experiment(base_url, num_iter=500):
    urls = gen_urls(base_url, num_iter)
    response_futures = chunked_requests(urls, 100)
    # response_futures 现在持有一个处于完成状态的迭代器， 所有这些futures的.value属性都有我们所期望的数据
    response_size = sum(len(r.value) for r in response_futures)
    return response_size


if __name__ == '__main__':
    import time

    delay = 100
    num_iter = 500
    base_url = f"http://127.0.0.1:8080/add?name=serial&delay={delay}"

    start = time.time()
    result = run_experiment(base_url, num_iter)
    end = time.time()
    print(f"Result:{result},{end - start}")
