from path_manager.product_tab.product_tab import ProductTab


class TabWithSingleResult(ProductTab):
    def __init__(self, name: str):
        super().__init__(name)

    def get_sub_dir(self) -> str:
        return ''
