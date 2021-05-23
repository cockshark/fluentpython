#! /usr/bin/python
# --*-- coding: utf-8 --*--
# ---------------------------
# @File Nme :  deal_task.py
# @Software : Pycharm
# @Desc : 
# @Author : 海心er
# @Date : 2021/5/23
# @Time : 23:16
# ---------------------------

__author__ = '海心er'

from loguru import logger

import time
from multiprocessing.managers import BaseManager

AUTHKEY = "crotia"


# 创建类似的manager
class Manager(BaseManager):
    pass


# 使用QueueManager 注册获取queue的方法名称
Manager.register('get_task_queue')
Manager.register('get_result_queue')

# 连接到服务器:
server_addr = '127.0.0.1'
logger.info('Connect to server %s...' % server_addr)

logger.info("端口和验证口令注意保持与服务进程设置的完全一致")
m = Manager(address=(server_addr, 8001), authkey=AUTHKEY.encode())

logger.info("从网络连接:")
m.connect()

logger.info("#获取Queue的对象:")
task = m.get_task_queue()
result = m.get_result_queue()

logger.info("从task队列取任务,并把结果写入result队列")
while not task.empty():
    image_url = task.get(True,timeout=5)
    logger.info('run task download %s...' % image_url)
    time.sleep(1)
    result.put('%s--->success' % image_url)


logger.info("worker exit.")