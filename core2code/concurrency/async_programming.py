"""
玩具意义的时间循环
"""

from queue import Queue

eventloop = None


class EventLoop(Queue):
    def start(self):
        while True:
            function = self.get()
            function()


def do_hello():
    global eventloop
    print("hello")
    eventloop.put(do_world)


def do_world():
    global eventloop
    print("world")
    eventloop.put(do_hello)


if __name__ == '__main__':
    eventloop = EventLoop()
    eventloop.put(do_hello)
    eventloop.start()
