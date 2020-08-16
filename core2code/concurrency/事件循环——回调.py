from functools import partial
from queue import Queue

eventloop = None


class EventLoop(Queue):
    def start(self):
        while True:
            function = self.get()
            function()


def save_value(value, callback):
    print(f"saving {value} to database")
    save_result_to_db(result, callback)
    # 是一个异步函数，他会立即返回并且结束，允许其他代码运行。无论如何，一旦数据准备好 print_response 就会被调用


def print_response(db_response):
    print(f"Response from database:{db_response}")


if __name__ == '__main__':
    eventloop = EventLoop()
    eventloop.put(partial(save_value, "Hello World", print_response))
