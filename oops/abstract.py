from abc import ABC, abstractmethod


class TheThread(ABC):

    @abstractmethod
    def run():
        pass

    pass


obj = TheThread()