from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside absclass task")
class testclass(Absclass):
    def task(self):
        print("We are inside testclass task")
test_obj = testclass()
test_obj.task()
test_obj.print(100)