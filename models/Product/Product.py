from openpyxl.cell.cell import Cell

class Product:
    ID_COLUMN_INDEX = 0
    CATEGORY_COLUMN_INDEX = 5

    def __init__(self, row: tuple[Cell]):
        self._row = row

        self.id = self._row[self.ID_COLUMN_INDEX].value
        self.category = self._row[self.CATEGORY_COLUMN_INDEX].value
