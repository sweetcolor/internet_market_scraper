import abc


class ProductTab(abc.ABC):
    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def get_sub_dir(self) -> str:
        pass
