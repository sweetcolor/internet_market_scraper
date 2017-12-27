import abc


class ProductTab(abc.ABC):
    def __init__(self, name: str):
        self.name = name

    @abc.abstractclassmethod
    def get_sub_dir(self) -> str:
        pass
