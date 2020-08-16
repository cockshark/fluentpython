"""
grequests 组合了HTTP库请求和gevent， 其结果就是具有很简单的API来做并发HTTP请求（甚至为我们处理信号量）
代码更简单，容易理解，可维护性更好，也能有使用更底层的gevent代码相同的速度提升

"""
import grequests
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
    response_futures = (grequests.get(u) for u in urls)
    # 首先我们创建了请求并且得到了future， 我们选择把他当作生成器generator来做， 这样以后我们只需要做与我们发出的请求相同次数的估算
    responses = grequests.imap(response_futures, size=100)
    # 现在我们能够取得future对象， 并把他们映射成真实的响应对象。.imap函数给我们一个生成器generator来产生响应对象， 我们从响应对象获取数据
    response_size = sum(len(r.text) for r in responses)
    return response_size
