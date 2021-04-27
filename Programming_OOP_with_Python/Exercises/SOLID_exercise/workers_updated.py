from abc import abstractmethod, ABC
import time


class Workable:
    def __init__(self):
        self.worker = None

    @abstractmethod
    def work(self):
        pass

    def set_worker(self, worker):
        self.worker = worker

    def manage(self):
        print(self.worker.work())


class Eatable(Workable, ABC):

    @abstractmethod
    def eat(self):
        pass

    def lunch_break(self):
        print(self.worker.eat())


class SuperWorker(Eatable):

    def work(self):
        return "I'm super worker. I work very hard!"

    def eat(self):
        return "Lunch break....(3 secs)"


class Worker(Eatable):
    def work(self):
        return f'Im normal worker. Im working.'

    def eat(self):
        return f'Lunch break....(5 secs)'


class WorkManager(Eatable):
    def work(self):
        return f'Im work manager. Im command the workers.'

    def eat(self):
        return f'Lunch break....(5 secs)'


class BreakManager(Eatable):
    def work(self):
        return f'Im break manager. Im chilling.'

    def eat(self):
        return f'Lunch break....(5 secs)'


class Manager(Eatable):

    def work(self):
        return 'I am manager and I control people'

    def eat(self):
        return 'I eat for 5 seconds'


class Robot(Workable):
    def work(self):
        return "I'm a robot. I'm working...."


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
