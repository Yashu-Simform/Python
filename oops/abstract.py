from abc import ABC, abstractmethod

class TheThread(ABC):
    @abstractmethod
    def run():
        print('Hello')
        return 5
        pass


class MyThread(TheThread):

    def run():
        pass

    def walk():
        print('Me Hoon Na!')

# o1 = TheThread()
obj = MyThread()
# obj.run()
