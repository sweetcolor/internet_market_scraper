import abc


class OutputFile(abc.ABC):
    def __init__(self, extension: str, ):
        self.ext = extension
