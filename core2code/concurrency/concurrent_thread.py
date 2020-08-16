"""多线程编程"""

import concurrent.futures
import requests
import threading


def download(url: str):
    resp = requests.get(url=url)
    print(f"read {len(resp.content)} from {url}")


def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download, sites)


# ---------------------------------------------------------------------------------

def download_all_1(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download, site)
            to_do.append(future)

        for future in concurrent.futures.as_completed(to_do):
            future.result()



"""
函数说明
executor.submit(func)执行时候， 她便会安排里面的func()函数执行，并返回创建好的future实例，方便你之后查询调用

done() 可以被future的实例调用 表示相对应的操作是否完成。不过这个方法是Non-blocking（非阻塞）的会立即返回结果。
相对应的add_done_callback(fn),则表示Futures完成后， 相应的参数函fn，会被通知并执行调用。————这个是不是挺有用的

result() 可以被future实例调用， 他表示当future完成后，返回其对应的结果或者异常。
as_completed是futures内实现的一个方法，as_completed(fs),传入一个task序列，序列里是组装好的future实例——针对给定的future迭代器fs
        在其完成后，返回完成后的迭代器
"""