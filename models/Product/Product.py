from openpyxl.cell.cell import Cell

class Product:
    ID_COLUMN_INDEX = 1

    def __init__(self, row: tuple[Cell]):
        self._row = row

    def _setup(self):
        self._product_id = self._get_product_id()

    def _get_product_id(self):
        product_id = self._row[self.ID_COLUMN_INDEX].value

        return product_id

