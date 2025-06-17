from abc import ABC, abstractmethod

class TheThread(ABC):
    @abstractmethod
    def run():
        print('Hello')
        return 5


class MyThread(TheThread):

    def run():
        print('Hi')

    def walk():
        print('Me Hoon Na!')

# o1 = TheThread()
# obj = MyThread()
# obj.run()
TheThread.run()
