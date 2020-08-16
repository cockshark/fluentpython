from functools import partial
from queue import Queue

eventloop = None


class EventLoop(Queue):
    def start(self):
        while True:
            function = self.get()
            function()

@coroutine
def save_value(value, callback):
    print(f"saving {value} to database")
    db_response = yield save_result_to_db(result, callback)
    # 这种情况下， 该海曙返回了一个Future类型。通过让步(yieldiing)，我们就确保暂停了save_value，直到值准备好了才继续并完成它的操作
    print(f"Response from databse :{db_response}")
