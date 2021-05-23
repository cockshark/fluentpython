#! /usr/bin/python
# --*-- coding: utf-8 --*--
# ---------------------------
# @File Nme :  task_queue.py
# @Software : Pycharm
# @Desc : 
# @Author : 海心er
# @Date : 2021/5/23
# @Time : 22:51
# ---------------------------

__author__ = '海心er'

from loguru import logger

from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from multiprocessing import Queue

# 任务个数
TASK_NUMBER = 10

AUTHKEY = "crotia"

# 发送 接收 队列
TASK_QUEUE = Queue(TASK_NUMBER)
RESULT_QUEUE = Queue(TASK_NUMBER)


def get_task():
    return TASK_QUEUE


def get_result():
    return RESULT_QUEUE


# 创建类似的queuemannager
class QueueManager(BaseManager):
    pass


def win_run():
    # 注册在网络上，callable 关联了Queue 对象
    # 将Queue对象在网络中暴露
    # window下绑定调用接口不能直接使用lambda，所以只能先定义函数再绑定
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)

    # 绑定端口和设置验证口令
    manager = QueueManager(address=('127.0.0.1', 8001), authkey=AUTHKEY.encode())

    # 启动管理，监听信息通道
    manager.start()

    try:
        # 通过网络获取任务队列和结果队列
        task = manager.get_task_queue()
        result = manager.get_result_queue()

        # 添加任务
        for url in ["ImageUrl_" + str(i) for i in range(10)]:
            logger.debug('url is %s' % url)
            task.put(url)

        logger.info("try get result")

        for i in range(10):
            logger.info('result is %s' % result.get(timeout=10))
    except Exception as ex:  # todo fix with concrete error
        logger.error("manager error")
    finally:
        logger.info("end manager")
        manager.shutdown()


if __name__ == '__main__':
    freeze_support()
    win_run()
