from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("reading data from network")


# because we @abstractmethod the read() method, every time
# we create a new class which inherits from Stream needs
# to have a read method

class MemomeryStream(Stream):
    def read(self):
        print("reading from memory")


stream = MemomeryStream()
stream.open()
