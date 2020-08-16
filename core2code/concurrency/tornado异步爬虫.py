"""
python 中很频繁使用的异步IO包是tornado。 对比gevent， tornado选择使用回调的方式来做异步行为
"""

from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

from functools import partial
import string
import random

AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient", max_clients=100)
# 配置HTTP客户端并挑选我们希望使用的后台库， 以及我们想要批量处理的请求数量


def gen_urls(base_urls, num_urls):
    for i in range(num_urls):
        yield base_urls + "".join(random.sample(string.ascii_lowercase, 10))


@gen.coroutine
def run_experiment(base_url, num_iter=500):
    http_client = AsyncHTTPClient()
    urls = gen_urls(base_url, num_iter)
    responses = yield [http_client.fetch(url) for url in urls]
    # 生成了许多futures， 解这yield回到IO循环中，这个函数会继续， responses变量会被所有的futures填充， 当他们就绪时，产生结果
    response_sum = sum(len(r.value) for r in responses)
    raise gen.Return(value=response_sum)
    # 在tornado中的携程由python的生成器来支持。为了从它们返回值，我们必须要生成一个特殊的异常，由gen.coroutine把它转化成一个返回值


if __name__ == '__main__':
    # initialize 。。。。
    _ioloop = ioloop.IOLoop.instance()
    run_func = partial(run_experiment, base_url, num_iter)
    result = _ioloop.run_sync(run_func)
    # ioloop。run_sync会只在特殊化的函数.ioloop.start()的运行时间段内启动ioloop， 另一方面，启动了一个必须手动停止的IOLoop