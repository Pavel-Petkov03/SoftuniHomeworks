from abc import ABC, abstractmethod


class Worker(ABC):
    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(Worker):
    def work(self):
        print("I work very hard!!!")


class LazyWorker(Worker):
    def work(self):
        print('I am too lazy to work')


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
super_worker = LazyWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
